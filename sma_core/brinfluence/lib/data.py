import os
from brinfluence.lib import parse_data

'''
generates parsed(stripped) data about user and puts it in sma_data folder inside every user's directory
with files that contain media, comments and emojis data that user has shared on Instagram
'''
def generate_sma_data(root_dir):
    for subdir in os.listdir(root_dir):
        if subdir == 'Brands':
            path = root_dir + "\Brands"
            for brand in os.listdir(path):
                path_to_brand = path + "\\" + brand

                write_sma_data_to_file(path_to_brand)

        if subdir == 'Users':
            path = root_dir + "\\Users"
            for user in os.listdir(path):
                path_to_user = path + "\\" + user

                write_sma_data_to_file(path_to_user)

'''
returns 2D matrix of users/brands' sma_data with pattern: username, media, comments, media_emojis, comments_emojis
'''
def retrieve_sma_data(root_dir, user_type):
    row = []
    data_matrix = []

    for subdir in os.listdir(root_dir + "\\" + user_type):
        path_to_user = root_dir + "\\" + user_type + "\\" + subdir
        path_to_data = path_to_user + "\sma_data"

        if os.path.exists(path_to_data):
            username = subdir.replace("@", "")
            row.append(username)

            with open(path_to_data + '\media.txt', 'r', encoding="utf-8") as f:
                media = f.read().replace('\n', '')

            row.append(media)

            with open(path_to_data + '\comments.txt', 'r', encoding="utf-8") as f:
                comments = f.read().replace('\n', '')

            row.append(comments)

            with open(path_to_data + '\media_emojis.txt', 'r', encoding="utf-8") as f:
                media_emojis = f.read().replace('\n', '')

            row.append(media_emojis)

            with open(path_to_data + '\comments_emojis.txt', 'r', encoding="utf-8") as f:
                comments_emojis = f.read().replace('\n', '')

            row.append(comments_emojis)

            data_matrix.append(row)
            row = []

    return data_matrix


def write_sma_data_to_file(path):
    new_dir = path + "\sma_data"

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

        user_media_data = parse_data.get_user_media_captions(path)
        user_media_emojis = parse_data.get_user_media_emojis(path)
        user_comments_data = parse_data.get_user_comments(path)
        user_comments_emojis = parse_data.get_user_comments_emojis(path)

        print(user_media_data, file=open(new_dir + "\media.txt", 'w', encoding="utf-8"))
        print(user_media_emojis, file=open(new_dir + "\media_emojis.txt", 'w', encoding="utf-8"))
        print(user_comments_data, file=open(new_dir + "\comments.txt", 'w', encoding="utf-8"))
        print(user_comments_emojis, file=open(new_dir + "\comments_emojis.txt", 'w', encoding="utf-8"))
