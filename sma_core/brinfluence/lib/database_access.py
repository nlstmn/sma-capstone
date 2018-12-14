import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sma_core.settings")
django.setup()

from brinfluence.lib import parse_data
from brinfluence.lib import data_utils
from brinfluence.lib import static_data
from brinfluence.models import *


'''
Updates database if new user/s or brand/s is added to dataset folder. Info: No sma_data folder needed!
Gets original data from .json files of users & brands and initializes corresponding model and its fields.
Using Manager class of each model, user/brand data is entered into database.
'''
def add_objects(root_dir):
    print("New users/brands are being added to database. Please wait...\n")
    # Iterate through every sub folder of root directory | subdir=['Users','Brands']
    for subdir in os.listdir(root_dir):
        if subdir == 'Brands':
            saved_brands = []
            # Get all brand objects from database and add their usernames to a list
            for brand in Brand.objects.all():
                saved_brands.append(brand.username)

            path = root_dir + "\\Brands"
            # Iterate through every brand in dataset
            for brand in os.listdir(path):
                username = parse_data.get_username(path + "\\" + brand)

                # Check whether brand was already in database, if not add brand to database
                if username not in saved_brands:
                    print("Adding brand: " + username)

                    data = parse_data.get_profile_data(path + "\\" + brand)

                    try:
                        biography = data['biography']
                    except KeyError:
                        try:
                            biography = data['graphql']['user']['biography']
                        except KeyError:
                            biography = "no biography"

                    try:
                        email = data['email']
                    except KeyError:
                        email = "unknown"

                    try:
                        gender = data['gender']
                    except:
                        gender = "unspecified"

                    try:
                        name = data['name']
                    except KeyError:
                        try:
                            name = data['graphql']['user']['full_name']
                        except KeyError:
                            name = "unspecified"

                    try:
                        profile_pic_url = data['profile_pic_url']
                    except KeyError:
                        profile_pic_url = data['graphql']['user']['profile_pic_url']


                    try:
                        business_category = data['business_category']
                    except KeyError:
                        try:
                            if data['graphql']['user']['business_category_name'] is not None:
                                business_category = data['graphql']['user']['business_category_name']
                            else:
                                business_category = "unspecified"
                        except KeyError:
                            business_category = "unspecified"

                    try:
                        business_city = data['business_city']
                    except KeyError:
                        business_city = "unspecified"

                    try:
                        business_email = data['business_email']
                    except KeyError:
                        try:
                            if data['graphql']['user']['business_email'] is not None:
                                business_email = data['graphql']['user']['business_email']
                            else:
                                business_email = "unspecified"
                        except KeyError:
                            business_email = "unspecified"

                    biography = data_utils.remove_new_line(biography)

                    # Create brand object and add it to database
                    Brand.objects.create_brand(biography, email, gender, name, profile_pic_url, username,
                                               business_category, business_city, business_email)

                    # Get instance of newly created brand object from database
                    brand_object = Brand.objects.filter(username=username)[:1].get()

                    media = parse_data.get_user_media_list(path + "\\" + brand)

                    # Iterate through every post shared by brand
                    for post in media:
                        # Check whether post has caption or location, otherwise skip it (skip posts without caption[:0]
                        # and no location[:1] specified)
                        if not (post[0] == '' and post[1] == 'location unknown'):
                            if post[0] == '':
                                caption = 'no caption'
                            else:
                                caption = post[0]

                            caption = data_utils.remove_new_line(caption)
                            location = post[1]

                            # Create brand media object and add it to database
                            BrandMedia.objects.create_brand_media(brand_object, caption, location)

                    comments = parse_data.get_user_comments_list(path + "\\" + brand)

                    # Iterate through every comment made by brand
                    for comment in comments:
                        comment_text = comment[0]
                        commented_on = comment[1]

                        # Create brand comment object and add it to database
                        BrandComment.objects.create_brand_comment(brand_object, comment_text, commented_on)

                    print("Brand " + username + " has been added.\n")

        if subdir == 'Users':
            saved_users = []
            # Get all user objects from database and add their usernames to a list
            for user in User.objects.all():
                saved_users.append(user.username)

            path = root_dir + "\\Users"
            # Iterate through every user in dataset
            for user in os.listdir(path):
                username = parse_data.get_username(path + "\\" + user)

                # Check whether user was already in database, if not add user to database
                if username not in saved_users:
                    print("Adding influencer: " + username)
                    data = parse_data.get_profile_data(path + "\\" + user)

                    try:
                        biography = data['biography']
                    except KeyError:
                        try:
                            biography = data['graphql']['user']['biography']
                        except KeyError:
                            biography = "no biography"

                    try:
                        email = data['email']
                    except KeyError:
                        email = "unknown"

                    try:
                        gender = data['gender']
                    except KeyError:
                        gender = "unspecified"

                    try:
                        name = data['name']
                    except KeyError:
                        try:
                            name = data['graphql']['user']['full_name']
                        except KeyError:
                            name = "unspecified"

                    try:
                        profile_pic_url = data['profile_pic_url']
                    except KeyError:
                        profile_pic_url = data['graphql']['user']['profile_pic_url']

                    try:
                        date_of_birth = data['date_of_birth']
                    except KeyError:
                        date_of_birth = "1970-01-01"

                    biography = data_utils.remove_new_line(biography)

                    # Create user object and add it to database
                    User.objects.create_user(biography, email, gender, name, profile_pic_url, username, date_of_birth)

                    # Get instance of newly created user object from database
                    user_object = User.objects.filter(username=username)[:1].get()

                    media = parse_data.get_user_media_list(path + "\\" + user)

                    # Iterate through every post shared by user
                    for post in media:
                        # Check whether post has caption or location, otherwise skip it (skip posts without caption[:0]
                        # and no location[:1] specified)
                        if not (post[0] == '' and post[1] == 'location unknown'):
                            if post[0] == '':
                                caption = 'no caption'
                            else:
                                caption = post[0]

                            caption = data_utils.remove_new_line(caption)
                            location = post[1]

                            # Create user media object and add it to database
                            UserMedia.objects.create_user_media(user_object, caption, location)

                    comments = parse_data.get_user_comments_list(path + "\\" + user)

                    # Iterate through every comment made by user
                    for comment in comments:
                        comment_text = comment[0]
                        commented_on = comment[1]

                        # Create brand comment object and add it to database
                        UserComment.objects.create_user_comment(user_object, comment_text, commented_on)

                    print("Influencer " + username + " has been added.\n")

    print("\nNew users/brands have been successfully added to database.")


def delete_object():
    continue_ = '1'
    while continue_ == '1':
        username = input("\nEnter username of object to be deleted: ")
        option = input("Is object to be deleted brand (1) or user (2)? ")
        if option == '1':
            Brand.objects.get(username=username).delete()
            print("\n" + username + " has been deleted from database.")
        else:
            User.objects.get(username=username).delete()
            print("\n" + username + " has been deleted from database.")

        continue_ = input("If you want to continue enter 1... ")


root_dir = static_data.get_dataset_root_dir()
option = input("Enter 1 to add objects to database\nEnter 2 to delete object from database\n")

if option == '1':
    add_objects(root_dir)
else:
    delete_object()
