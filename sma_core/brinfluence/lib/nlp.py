import os
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
import numpy as np
from nltk.stem import WordNetLemmatizer
from gensim import corpora
from gensim import models
from gensim.utils import simple_preprocess
from brinfluence.lib import data, nlp_utils


root_dir = input("Enter root directory of Instagram dataset: ")


# Returns tokenized list from all users/brands based on user type and document name
# User type can be Users or Brands | Document name can be media.txt, comments.txt etc
def get_tokenized_list(root_dir, user_type, doc_type):
    path = root_dir + "\\" + user_type

    tokenized_list = []
    for user in os.listdir(path):
        path_to_user = path + "\\" + user

        list = simple_preprocess(data.get_doc(path_to_user, doc_type))
        tokenized_list.append(list)

    return tokenized_list


# Create dictionary by using ReadTxtFiles class
dictionary = corpora.Dictionary(nlp_utils.ReadTxtFiles(root_dir, "Users", "media.txt"))
print("\nUsers category - distinct words")
print(dictionary)

print("\nUsers category - tokenized list")
tokenized_list = get_tokenized_list(root_dir, 'Users', "media.txt")
print(tokenized_list)

# Create corpus from dictionary
corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in tokenized_list]
print("\n Users category - corpus")
print(corpus)

# Decode corpus using dictionary
word_counts = [[(dictionary[id], count) for id, count in line] for line in corpus]
print("\n Users category - decoded corpus (word counts)")
print(word_counts)

# Create Bag of Words corpus for Users category
bow_corpus = nlp_utils.BoWCorpus(root_dir, "Users", dictionary, "media.txt")
print("\nUsers category - bag of words corpus")
for line in bow_corpus:
    print(line)

word_counts = [[(dictionary[id], count) for id, count in line] for line in bow_corpus]
print("\nUsers category - decoded bag of words corpus (word counts)")
for line in word_counts:
    print(line)

print("\nTFDIF Weighted decoded bag of words corpus")
tfdif = models.TfidfModel(bow_corpus, smartirs='ntc')
for doc in tfdif[bow_corpus]:
    print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
print("\n--->")


# Returns tokenized list from specific user/brand based on document name
# Document name can be media.txt, comments.txt etc
def get_user_tokenized_list(root_dir, user_type, username, doc_name):
    path_to_user = root_dir + "\\" + user_type + "\\" + username
    tokenized_list = []
    list = simple_preprocess(data.get_doc(path_to_user, doc_name))
    tokenized_list.append(list)
    return tokenized_list


# Get tokenized list for username liana.nsan
tokenized_list = get_user_tokenized_list(root_dir, "Users", "@liana.nsan", "media.txt")
print("\n@liana.nsan - tokenized list")
print(tokenized_list)

# Create corpus for username liana.nsan
corpus = [dictionary.doc2bow(doc, allow_update=False) for doc in tokenized_list]
print("\n@liana.nsan - corpus")
print(corpus)

# Decode corpus using dictionary
word_counts = [[(dictionary[id], count) for id, count in line] for line in corpus]
print("\n@liana.nsan - decoded corpus (word counts)")
print(word_counts)
