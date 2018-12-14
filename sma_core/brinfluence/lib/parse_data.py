import json
import codecs
from brinfluence.lib import data_utils


# Returns all post's captions written by specific user
# (parsed captions without stopwords, special characters, numbers and emojis)
def get_user_media_captions(path):
    meta = 0

    path_to_file = path + "\media.json"

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        path_to_file = path + "\metadata.json"
        with open(path_to_file, mode="r", encoding="utf-8") as f:
            data = json.load(f)

        meta = 1

    decoded_data = ""
    if meta == 0:
        for item in data['photos']:
            decoded_data += item['caption'] + ' '
    else:
        for entity in data:
            for media in entity['edge_media_to_caption']['edges']:
                decoded_data += media['node']['text'] + ' '

    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.remove_emojis(decoded_data)
    decoded_data = data_utils.remove_numbers(decoded_data)
    decoded_data = data_utils.remove_braille_pattern(decoded_data)

    decoded_data = decoded_data.lower()
    #decoded_data = data_utils.remove_stopwords(decoded_data)
    decoded_data = data_utils.remove_multiple_whitespace(decoded_data)
    #decoded_data = data_utils.lemmatize(decoded_data)

    return decoded_data


# Returns list of all shared media for a specific user
# containing caption & location of all pictures (as originally posted)
def get_user_media_list(path):
    meta = 0
    path_to_file = path + "\media.json"

    try:
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
    except FileNotFoundError:
        path_to_file = path + "\metadata.json"
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
        meta = 1

    post = []
    media = []

    if meta == 0:
        for item in data['photos']:
            post.append(item['caption'])

            try:
                post.append(item['location'])
            except KeyError:
                post.append('location unknown')

            media.append(post)
            post = []
    else:
        for entity in data:
            for item in entity['edge_media_to_caption']['edges']:
                post.append(item['node']['text'])
                post.append('location unknown')

                media.append(post)
                post = []

    return media


# Returns list of all emojis user has used in its posts
def get_user_media_emojis(path):
    meta = 0
    path_to_file = path + "\media.json"

    try:
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
    except FileNotFoundError:
        path_to_file = path + "\metadata.json"
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
        meta = 1

    decoded_data = ""
    if meta == 0:
        for item in data['photos']:
            decoded_data += item['caption'] + ' '
    else:
        for entity in data:
            for media in entity['edge_media_to_caption']['edges']:
                decoded_data += media['node']['text'] + ' '

    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.get_emojis(decoded_data)

    return decoded_data


# Returns all comments made by specific user
# (parsed comments without stopwords, special characters, numbers and emojis)
def get_user_comments(path):
    meta = 0
    path_to_file = path + "\comments.json"

    try:
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
    except FileNotFoundError:
        path_to_file = path + "\metadata.json"
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
        meta = 1

    decoded_data = ""
    if meta == 0:
        for item in data['media_comments']:
            decoded_data += item[1] + ' '
    else:
        for entity in data:
            for comment in entity['comments']['data']:
                decoded_data += comment['text'] + ' '

    decoded_data = data_utils.remove_user_tags(decoded_data)
    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.remove_emojis(decoded_data)
    decoded_data = data_utils.remove_numbers(decoded_data)
    decoded_data = data_utils.remove_braille_pattern(decoded_data)

    decoded_data = decoded_data.lower()
    decoded_data = data_utils.remove_stopwords(decoded_data)
    decoded_data = data_utils.remove_multiple_whitespace(decoded_data)
    decoded_data = data_utils.lemmatize(decoded_data)

    return decoded_data


# Returns list of all comments made by a specific user
# containing comment & commented_on fields (as originally commented)
def get_user_comments_list(path):
    meta = 0
    path_to_file = path + "\comments.json"

    try:
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
    except FileNotFoundError:
        path_to_file = path + "\metadata.json"
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
        meta = 1

    comment = []
    media_comments = []

    if meta == 0:
        for item in data['media_comments']:
            try:
                comment.append(item[1])
                comment.append(item[2])

                media_comments.append(comment)
                comment = []
            except IndexError:
                pass
    else:
        try:
            for entity in data:
                for item in entity['comments']['data']:
                    comment.append(item['text'])
                    comment.append(item['owner']['username'])

                    media_comments.append(comment)
                    comment = []
        except KeyError:
            pass

    return media_comments


# Returns list of all emojis user has used in the comments he/she made
def get_user_comments_emojis(path):
    meta = 0
    path_to_file = path + "\comments.json"

    try:
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
    except FileNotFoundError:
        path_to_file = path + "\metadata.json"
        data = json.load(codecs.open(path_to_file, 'r', 'utf-8-sig'))
        meta = 1

    decoded_data = ""
    if meta == 0:
        for item in data['media_comments']:
            decoded_data += item[1] + ' '
    else:
        for entity in data:
            for comment in entity['comments']['data']:
                decoded_data += comment['text'] + ' '

    decoded_data = data_utils.remove_special_char(decoded_data)
    decoded_data = data_utils.get_emojis(decoded_data)

    return decoded_data


# Returns username field, given a path to user, from profile.json file
def get_username(path_to_user):
    path_to_user = path_to_user + "\\profile.json"

    with open(path_to_user, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        username = data['username']
    except KeyError:
        username = data['graphql']['user']['username']

    return username


# Returns user all profile data given a path to user
def get_profile_data(path):
    path = path + "\profile.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    return data


# Returns media.json for a specific user
def get_user_media_json(path):
    path = path + "\media.json"

    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    return data
