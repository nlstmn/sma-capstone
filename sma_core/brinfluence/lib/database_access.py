import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sma_core.settings")
django.setup()

from brinfluence.lib import parse_data
from brinfluence.lib import data_utils
from brinfluence.models import *

'''
Updates database if new user/s or brand/s is added to dataset folder. Info: No sma_data folder needed!
Gets original data from .json files of users & brands and initializes corresponding model and its fields.
Using Manager class of each model, user/brand data is entered into database.
'''
root_dir = input("Enter root dir:")

print("New users/brands are being added to database. Please wait...")
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
                data = parse_data.get_profile_data(path + "\\" + brand)

                try:
                    biography = data['biography']
                except KeyError:
                    biography = "no biography"

                try:
                    email = data['email']
                except KeyError:
                    email = "unspecified"

                gender = data['gender']

                try:
                    name = data['name']
                except KeyError:
                    name = "unspecified"

                profile_pic_url = data['profile_pic_url']
                username = data['username']
                business_category = data['business_category']

                try:
                    business_city = data['business_city']
                except KeyError:
                    business_city = "unspecified"

                try:
                    business_email = data['business_email']
                except KeyError:
                    business_email = "unspecified"

                biography = data_utils.escape_new_line(biography)

                # Create brand object and add it to database
                Brand.objects.create_brand(biography, email, gender, name, profile_pic_url, username, business_category,
                                           business_city, business_email)

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

                        caption = data_utils.escape_new_line(caption)
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

                        caption = data_utils.escape_new_line(caption)
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
