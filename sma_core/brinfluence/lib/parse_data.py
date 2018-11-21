import json
from brinfluence.lib import data_utils


def get_user_media_captions(path):
    path = path + "\media.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    decoded_data = ""

    for item in data['photos']:
        decoded_data += item['caption'] + ' '

    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.remove_emojis(decoded_data)
    decoded_data = data_utils.remove_multiple_whitespace(decoded_data)
    decoded_data = data_utils.remove_numbers(decoded_data)

    decoded_data = decoded_data.lower()

    return decoded_data


def get_user_media_list(path):
    path = path + "\media.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    post = []
    media = []

    for item in data['photos']:
        post.append(item['caption'])

        try:
            post.append(item['location'])
        except KeyError:
            post.append('location unknown')

        media.append(post)
        post = []

    return media


def get_user_media_emojis(path):
    path = path + "\media.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    decoded_data = ""

    for item in data['photos']:
        decoded_data += item['caption'] + ' '

    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.get_emojis(decoded_data)

    return decoded_data


def get_user_comments(path):
    path = path + "\comments.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    print('\n')
    decoded_data = ""

    for item in data['media_comments']:
        decoded_data += item[1] + ' '

    decoded_data = data_utils.remove_user_tags(decoded_data)
    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.remove_emojis(decoded_data)
    decoded_data = data_utils.remove_multiple_whitespace(decoded_data)
    decoded_data = data_utils.remove_numbers(decoded_data)

    decoded_data = decoded_data.lower()

    return decoded_data


def get_user_comments_list(path):
    path = path + "\comments.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    comment = []
    media_comments = []

    for item in data['media_comments']:
        comment.append(item[1])
        comment.append(item[2])

        media_comments.append(comment)
        comment = []

    return media_comments


def get_user_comments_emojis(path):
    path = path + "\comments.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    decoded_data = ""

    for item in data['media_comments']:
        decoded_data += item[1] + ' '

    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.get_emojis(decoded_data)

    return decoded_data


def get_username(path):
    path = path + "\profile.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    decoded_data = data['username']
    return decoded_data


def get_profile_data(path):
    path = path + "\profile.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    return data
