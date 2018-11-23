import os
from smart_open import smart_open
from gensim.utils import simple_preprocess


# Read a file line-by-line and uses gensim’s simple_preprocess to process one line of the file at a time
# Read an entire text file without loading the file in memory all at once
# Used for specific category: Users or Brands
class ReadTxtFiles(object):
    def __init__(self, root_dir, user_type, doc_name):
        self.root_dir = root_dir
        self.user_type = user_type
        self.doc = doc_name

    def __iter__(self):
        for user in os.listdir(self.root_dir + "\\" + self.user_type):
            path = self.root_dir + "\\" + self.user_type + "\\" + user + "\\sma_data\\" + self.doc
            for line in open(path, encoding="utf-8"):
                yield simple_preprocess(line)


# Read a file line-by-line and uses gensim’s simple_preprocess to process one line of the file at a time
# Read an entire text file without loading the file in memory all at once
# Used for all categories: Users and Brands
class ReadTxtFilesAll(object):
    def __init__(self, root_dir, doc_name):
        self.root_dir = root_dir
        self.doc = doc_name

    def __iter__(self):
        for category in os.listdir(self.root_dir):
            for user in os.listdir(self.root_dir + "\\" + category):
                path = self.root_dir + "\\" + category + "\\" + user + "\\sma_data\\" + self.doc
                for line in open(path, encoding="utf-8"):
                    yield simple_preprocess(line)


# Reads the file one line at a time and yields a corpus object
# Read an entire text file without loading the file in memory all at once
# Used for specific category: Users or Brands
class BoWCorpus(object):
    def __init__(self, root_dir, user_type, dictionary, doc_name):
        self.root_dir = root_dir
        self.user_type = user_type
        self.dictionary = dictionary
        self.doc = doc_name

    def __iter__(self):
        for user in os.listdir(self.root_dir + "\\" + self.user_type):
            path = self.root_dir + "\\" + self.user_type + "\\" + user + "\\sma_data\\" + self.doc
            for line in smart_open(path, encoding="utf-8"):
                tokenized_list = simple_preprocess(line, deacc=True)

                bow = self.dictionary.doc2bow(tokenized_list, allow_update=True)
                yield bow
