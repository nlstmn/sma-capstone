import json
import codecs
from brinfluence.lib import data_utils


# Returns all post's captions written by specific user
# (parsed captions without special characters, numbers and emojis)
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


# Returns list of all shared media for a specific user
# containing caption & location of all pictures (as originally posted)
def get_user_media_list(path):
    path = path + "\media.json"

    data = json.load(codecs.open(path, 'r', 'utf-8-sig'))
    # with open(path, mode="r", encoding="utf-8") as f:
    #   data = json.load(f)

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


# Returns list of all emojis user has used in its posts
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


# Returns all comments made by specific user
# (parsed comments without special characters, numbers and emojis)
def get_user_comments(path):
    path = path + "\comments.json"

    data = json.load(codecs.open(path, 'r', 'utf-8-sig'))
    # with open(path, mode="r", encoding="utf-8") as f:
    #   data = json.load(f)

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


# Returns list of all comments made by a specific user
# containing comment & commented_on fields (as originally commented)
def get_user_comments_list(path):
    path = path + "\comments.json"

    data = json.load(codecs.open(path, 'r', 'utf-8-sig'))
    # with open(path, mode="r", encoding="utf-8") as f:
    #    data = json.load(f)

    comment = []
    media_comments = []

    for item in data['media_comments']:
        comment.append(item[1])
        comment.append(item[2])

        media_comments.append(comment)
        comment = []

    return media_comments


# Returns list of all emojis user has used in the comments he/she made
def get_user_comments_emojis(path):
    path = path + "\comments.json"

    data = json.load(codecs.open(path, 'r', 'utf-8-sig'))
    # with open(path, mode="r", encoding="utf-8") as f:
    #    data = json.load(f)

    decoded_data = ""

    for item in data['media_comments']:
        decoded_data += item[1] + ' '

    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.get_emojis(decoded_data)

    return decoded_data


# Returns username field, given a path to user, from profile.json file
def get_username(path_to_user):
    path_to_user = path_to_user + "\\profile.json"

    with open(path_to_user, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    username = data['username']
    return username


# Returns user all profile data given a path to user
def get_profile_data(path):
    path = path + "\profile.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def get_user_media_json(path):
    path = path + "\media.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    return data
