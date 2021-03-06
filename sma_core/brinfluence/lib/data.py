import os
import shutil
import gensim
from brinfluence.lib import parse_data


# Generates parsed(stripped) data about user and puts the data in sma_data folder inside every user's/brand's
# directory with files that contain media, comments and emojis data that user has shared on Instagram
# If user's/brand's sma_data already exits, it does not create files for that user
def generate_sma_data(root_dir):
    for subdir in os.listdir(root_dir):
        if subdir == 'Brands':
            path = root_dir + "\Brands"
            for brand in os.listdir(path):
                path_to_brand = path + "\\" + brand

                write_sma_data_to_file(path_to_brand, brand)

        if subdir == 'Users':
            path = root_dir + "\\Users"
            for user in os.listdir(path):
                path_to_user = path + "\\" + user

                write_sma_data_to_file(path_to_user, user)


# Returns 2D matrix of all users/brands' sma_data with columns: username, media, comments, media_emojis, comments_emojis
# User Type can be 'Brands' or 'Users'
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
            '''
            with open(path_to_data + '\comments.txt', 'r', encoding="utf-8") as f:
                comments = f.read().replace('\n', '')

            row.append(comments)

            with open(path_to_data + '\media_emojis.txt', 'r', encoding="utf-8") as f:
                media_emojis = f.read().replace('\n', '')

            row.append(media_emojis)

            with open(path_to_data + '\comments_emojis.txt', 'r', encoding="utf-8") as f:
                comments_emojis = f.read().replace('\n', '')

            row.append(comments_emojis)
            '''
            data_matrix.append(row)
            row = []

    return data_matrix


# Returns list of single user/brand' sma_data with columns: username, media, comments, media_emojis, comments_emojis
# User Type can be 'Brands' or 'Users"
def retrieve_user_sma_data(root_dir, user_type, username):
    row = []

    path_to_user = root_dir + "\\" + user_type + "\\" + username
    path_to_data = path_to_user + "\sma_data"

    if os.path.exists(path_to_data):
        username = username.replace("@", "")
        row.append(username)

        with open(path_to_data + '\media.txt', 'r', encoding="utf-8") as f:
            media = f.read().replace('\n', '')

        row.append(media)
    '''
        with open(path_to_data + '\comments.txt', 'r', encoding="utf-8") as f:
            comments = f.read().replace('\n', '')

        row.append(comments)

        with open(path_to_data + '\media_emojis.txt', 'r', encoding="utf-8") as f:
            media_emojis = f.read().replace('\n', '')

        row.append(media_emojis)

        with open(path_to_data + '\comments_emojis.txt', 'r', encoding="utf-8") as f:
            comments_emojis = f.read().replace('\n', '')

        row.append(comments_emojis)
    '''
    return row


# Deletes all sma_data for all users and brands
def delete_sma_data(root_dir):
    for subdir in os.listdir(root_dir):
        if subdir == 'Brands':
            path = root_dir + "\Brands"
            for brand in os.listdir(path):
                path_to_brand = path + "\\" + brand

                try:
                    shutil.rmtree(path_to_brand + "\\sma_data")
                except FileNotFoundError:
                    pass

        if subdir == 'Users':
            path = root_dir + "\\Users"
            for user in os.listdir(path):
                path_to_user = path + "\\" + user

                try:
                    shutil.rmtree(path_to_user + "\\sma_data")
                except FileNotFoundError:
                    pass


# Creates new sma_data folder and writes sma_data to a file given a path
# If sma_data folder already exits, files are not created
def write_sma_data_to_file(path, username):
    new_dir = path + "\sma_data"

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print("Generating sma_data: " + username)
        user_media_data = parse_data.get_user_media_captions(path)
        '''
        user_media_emojis = parse_data.get_user_media_emojis(path)
        user_comments_data = parse_data.get_user_comments(path)
        user_comments_emojis = parse_data.get_user_comments_emojis(path)
        '''

        print(user_media_data, file=open(new_dir + "\media.txt", 'w', encoding="utf-8"))
        '''
        print(user_media_emojis, file=open(new_dir + "\media_emojis.txt", 'w', encoding="utf-8"))
        print(user_comments_data, file=open(new_dir + "\comments.txt", 'w', encoding="utf-8"))
        print(user_comments_emojis, file=open(new_dir + "\comments_emojis.txt", 'w', encoding="utf-8"))
        '''
        print(username + ": sma_data has been generated.\n")


# Returns .txt file (doc) from a user's sma_data (doc_name can be media.txt, comments.txt etc)
def get_doc(path_to_user, doc_name):
    with open(path_to_user + "\\sma_data\\" + doc_name, 'r', encoding="utf-8") as f:
        data = f.read().replace('\n', '')

    return data


# Generates list of brands and users found in dataset
# Saves lists as users/brands.txt to dataset folder
def generate_user_brand_list(root_dir):
    for subdir in os.listdir(root_dir):
        if subdir == 'Brands':
            path = root_dir + "\\Brands"
            brand_list = ""
            for brand in os.listdir(path):
                brand_list = brand_list + brand + "\n"

            print(brand_list, file=open("dataset\\brands.txt", 'w', encoding="utf-8"))

        if subdir == 'Users':
            path = root_dir + "\\Users"
            user_list = ""
            for user in os.listdir(path):
                user_list = user_list + user + "\n"

            print(user_list, file=open("dataset\\users.txt", 'w', encoding="utf-8"))


# Shuffles the data for better accuracy, mixes brands and users accounts
# Returns matrix where it tries to make every even row to be user
# and every odd row to be brand
def shuffle_data(users_data, brands_data):
    data_matrix = []
    count = 0

    if len(brands_data) <= len(users_data):
        for i, row in enumerate(brands_data):
            data_matrix.append(row)
            data_matrix.append(users_data[i])
            count = i

        count = count + 1
        while count < len(users_data):
            data_matrix.append(users_data[count])
            count = count + 1
    else:
        for i, row in enumerate(users_data):
            data_matrix.append(row)
            data_matrix.append(brands_data[i])
            count = i

        count = count + 1
        while count < len(brands_data):
            data_matrix.append(brands_data[count])
            count = count + 1

    return data_matrix


# Saves words and their frequency based on gensim.Doc2Vec.model to dataset/common_words.txt
# count variable represents number of most frequent words to be saved
def generate_most_common_words(model_type, count):
    model = gensim.models.doc2vec.Doc2Vec.load('models\\' + model_type + '_model')
    row = []
    matrix = []

    for word, vocab_obj in model.wv.vocab.items():
        row.append(word)
        row.append(vocab_obj.count)
        matrix.append(row)
        row = []

    matrix.sort(key=lambda x: x[1], reverse=True)
    common_words = []
    for i, row in enumerate(matrix):
        common_words.append(row)
        if i == int(count):
            break

    with open('dataset\common_words_' + model_type + '.txt', 'w', encoding='utf-8') as f:
        for word in common_words:
            f.write(word[0] + "|" + str(word[1]) + "\n")
