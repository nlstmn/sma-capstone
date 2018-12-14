from django.shortcuts import render
from brinfluence.models import *
from brinfluence.lib import data, doc2vec, static_data

# Create your views here.


def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR'],
            'ua': request.META['HTTP_USER_AGENT']}


def home(request):
    context = ip_address_processor(request)
    user_list = User.objects.all().order_by('username')
    brand_list = Brand.objects.all().order_by('username')
    user_count = len(user_list)
    context.update({"users": user_list, "brands": brand_list, "user_count": user_count})
    return render(request, 'brinfluence/home.html', context)


def influencer_profile(request, username):
    user = User.objects.get(username=username)
    media = UserMedia.objects.filter(user=user)[:100]
    comments = UserComment.objects.filter(user=user)[:5]
    context = {"user": user, "comments": comments, "media": media}
    return render(request, 'brinfluence/influencer/profile.html', context)


def brand_profile(request, username):
    brand = Brand.objects.get(username=username)
    media = BrandMedia.objects.filter(brand=brand)[:100]
    comments = BrandComment.objects.filter(brand=brand)[:5]
    context = {"brand": brand, "comments": comments, "media": media}
    return render(request, 'brinfluence/brand/profile.html', context)


def influencer_recommended(request, username):
    root_dir = static_data.get_dataset_root_dir()
    model = doc2vec.get_model('brand')
    user_data = data.retrieve_user_sma_data(root_dir, 'Users', '@' + username)
    user_vector = doc2vec.get_user_vector(user_data, model)

    most_similar_brands = model.docvecs.most_similar(positive=[user_vector])

    recommended_brands = []
    row = []
    for brand in most_similar_brands:
        row.append(brand[0])
        row.append(round(brand[1] * 100, 2))
        recommended_brands.append(row)
        row = []

    user = User.objects.get(username=username)
    context = {"user": user, "recommended_brands": recommended_brands}
    return render(request, 'brinfluence/influencer/recommended.html', context)


def brand_recommended(request, username):
    root_dir = static_data.get_dataset_root_dir()
    model = doc2vec.get_model('user')
    brand_data = data.retrieve_user_sma_data(root_dir, 'Brands', '@' + username)
    brand_vector = doc2vec.get_user_vector(brand_data, model)

    most_similar_users = model.docvecs.most_similar(positive=[brand_vector])

    recommended_users = []
    row = []
    for user in most_similar_users:
        row.append(user[0])
        row.append(round(user[1] * 100, 2))
        recommended_users.append(row)
        row = []

    brand = Brand.objects.get(username=username)
    context = {"brand": brand, "recommended_users": recommended_users}
    return render(request, 'brinfluence/brand/recommended.html', context)


def influencer_similar(request, username):
    model = doc2vec.get_model('user')
    root_dir = static_data.get_dataset_root_dir()
    user_data = data.retrieve_user_sma_data(root_dir, 'Users', '@' + username)
    user_vector = doc2vec.get_user_vector(user_data, model)

    most_similar_influencers = model.docvecs.most_similar(positive=[user_vector])

    similar_users = []
    row = []
    for user in most_similar_influencers:
        row.append(user[0])
        row.append(round(user[1] * 100, 2))
        similar_users.append(row)
        row = []

    user = User.objects.get(username=username)
    context = {"user": user, "similar_users": similar_users}
    return render(request, 'brinfluence/influencer/similar.html', context)


def brand_similar(request, username):
    model = doc2vec.get_model('brand')
    root_dir = static_data.get_dataset_root_dir()
    brand_data = data.retrieve_user_sma_data(root_dir, 'Brands', '@' + username)
    brand_vector = doc2vec.get_user_vector(brand_data, model)

    most_similar_brands = model.docvecs.most_similar(positive=[brand_vector])

    similar_brands = []
    row = []
    for user in most_similar_brands:
        row.append(user[0])
        row.append(round(user[1] * 100, 2))
        similar_brands.append(row)
        row = []

    brand = Brand.objects.get(username=username)
    context = {"brand": brand, "similar_brands": similar_brands}
    return render(request, 'brinfluence/brand/similar.html', context)
