import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.utils import simple_preprocess
from gensim import corpora
from pprint import pprint
from brinfluence.lib import data


print("Enter path to a dataset directory such as C:\\Users\hp\Desktop\Instagram Dataset")
print("This directory should contain directories of different users with their Instagram data inside it.")
root_dir = input('Enter a path :')

data.generate_sma_data(root_dir)

data_matrix = data.retrieve_sma_data(root_dir)

print(data_matrix)

'''
users = [user1, user2]

texts = [[text for text in user.split()] for user in users]

dictionary = corpora.Dictionary(texts)

# Get information about the dictionary
print(dictionary)

print(dictionary.token2id)

tokenized_list = [simple_preprocess(user) for user in users]

mydict = corpora.Dictionary()
mycorpus = [mydict.doc2bow(user, allow_update=True) for user in tokenized_list]
pprint(mycorpus)
'''
