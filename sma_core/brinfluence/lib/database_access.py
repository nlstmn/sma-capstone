import os
import django
import pprint

from docutils.nodes import caption

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sma_core.settings")
django.setup()

from brinfluence.lib import parse_data
from brinfluence.lib import data_utils
from brinfluence.models import *

root_dir = input("Enter root dir:")

print("New users/brands are being added to database. Please wait...")
for subdir in os.listdir(root_dir):
    if subdir == 'Brands':
        saved_brands = []
        for brand in Brand.objects.all():
            saved_brands.append(brand.username)

        path = root_dir + "\Brands"
        for brand in os.listdir(path):
            username = brand.replace("@", "")

            if username not in saved_brands:
                data = parse_data.get_profile_data(path + "\\" + brand)

                biography = data['biography']
                email = data['email']
                gender = data['gender']
                name = data['name']
                profile_pic_url = data['profile_pic_url']
                username = data['username']
                business_category = data['business_category']
                business_city = data['business_city']
                business_email = data['business_email']

                biography = data_utils.escape_new_line(biography)

                Brand.objects.create_brand(biography, email, gender, name, profile_pic_url, username, business_category,
                                           business_city, business_email)

                brand_object = Brand.objects.filter(username=username)[:1].get()

                media = parse_data.get_user_media_list(path + "\\" + brand)

                for post in media:
                    if not (post[0] == '' and post[1] == 'location unknown'):
                        if post[0] == '':
                            caption = 'no caption'
                        else:
                            caption = post[0]

                        caption = data_utils.escape_new_line(caption)
                        location = post[1]

                        BrandMedia.objects.create_brand_media(brand_object, caption, location)

                comments = parse_data.get_user_comments_list(path + "\\" + brand)

                for comment in comments:
                    comment_text = comment[0]
                    commented_on = comment[1]

                    BrandComment.objects.create_brand_comment(brand_object, comment_text, commented_on)

    if subdir == 'Users':
        saved_users = []
        for user in User.objects.all():
            saved_users.append(user.username)

        path = root_dir + "\\Users"
        for user in os.listdir(path):
            username = user.replace("@", "")

            if username not in saved_users:
                data = parse_data.get_profile_data(path + "\\" + user)

                biography = data['biography']
                email = data['email']
                gender = data['gender']

                try:
                    name = data['name']
                except KeyError:
                    name = "unspecified"

                profile_pic_url = data['profile_pic_url']
                username = data['username']

                try:
                    date_of_birth = data['date_of_birth']
                except KeyError:
                    date_of_birth = "1970-01-01"

                biography = data_utils.escape_new_line(biography)

                User.objects.create_user(biography, email, gender, name, profile_pic_url, username, date_of_birth)

                user_object = User.objects.filter(username=username)[:1].get()

                media = parse_data.get_user_media_list(path + "\\" + user)

                for post in media:
                    if not (post[0] == '' and post[1] == 'location unknown'):
                        if post[0] == '':
                            caption = 'no caption'
                        else:
                            caption = post[0]

                        caption = data_utils.escape_new_line(caption)
                        location = post[1]

                        UserMedia.objects.create_user_media(user_object, caption, location)

                comments = parse_data.get_user_comments_list(path + "\\" + user)

                for comment in comments:
                    comment_text = comment[0]
                    commented_on = comment[1]

                    UserComment.objects.create_user_comment(user_object, comment_text, commented_on)
