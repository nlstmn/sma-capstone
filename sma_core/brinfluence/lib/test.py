import warnings
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora
from brinfluence.lib import data


root_dir = input("Enter root directory of Instagram dataset: ")

# Retrieve sma_data from users category into a matrix
data_matrix = data.retrieve_sma_data(root_dir, 'Users')

documents = []

# Create documents list of only media.txt files (row[1])
for row in data_matrix:
    documents.append(row[1])

# Split documents and then extract words from document (without using nltk library) - matrix
texts = [[text for text in doc.split()] for doc in documents]

# Create dictionary
dictionary = corpora.Dictionary(texts)
print('\n')
print("Users category - distinct words")
print(dictionary)

wordnet_lemmatizer = WordNetLemmatizer()

print("\nMaking lemmatization (Users)...")
lemmatization_documents = []

for doc in documents:
    # Use nltk library to extract words from document
    sentence_words = nltk.word_tokenize(doc)

    # Transform every word into root word (lemmatization)
    for word in sentence_words:
        doc = doc.replace(word, wordnet_lemmatizer.lemmatize(word, pos='v'))
    lemmatization_documents.append(doc)

# Split lemmatization_documents and then extract words from document (without using nltk library) - matrix
texts = [[text for text in doc.split()] for doc in lemmatization_documents]
dictionary = corpora.Dictionary(texts)
print("\nUsers category - distinct words after lemmatization")
print(dictionary)

print("\n--->")
# Retrieve sma_data from brands category into a matrix
data_matrix = data.retrieve_sma_data(root_dir, 'Brands')

documents = []

# Create documents list of only media.txt files (row[1])
for row in data_matrix:
    documents.append(row[1])

# Split documents and then extract words from document (without using nltk library) - matrix
texts = [[text for text in doc.split()] for doc in documents]

# Create dictionary
dictionary = corpora.Dictionary(texts)
print('\n')
print("Brands category - distinct words")
print(dictionary)

print("\nMaking lemmatization (Brands)...")
lemmatization_documents = []

for doc in documents:
    # Use nltk library to extract words from document
    sentence_words = nltk.word_tokenize(doc)

    # Transform every word into root word (lemmatization)
    for word in sentence_words:
        doc = doc.replace(word, wordnet_lemmatizer.lemmatize(word, pos='v'))
    lemmatization_documents.append(doc)

# Split lemmatization_documents and then extract words from document (without using nltk library) - matrix
texts = [[text for text in doc.split()] for doc in lemmatization_documents]
dictionary = corpora.Dictionary(texts)
print("\nBrands category - distinct words after lemmatization")
print(dictionary)


sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
print("\nExample of lemmatization: " + sentence)
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word, pos="v")))

# Removing stop words from a document
stop_words = set(stopwords.words('english'))

data_matrix = data.retrieve_sma_data(root_dir, 'Users')

documents = []
print("\nList of users media words: ")
for row in data_matrix:
    words = row[1].split()
    print(words)
    for word in words:
        if word in stop_words:
            row[1] = row[1].replace(word, "")

    documents.append(row[1])

print('\nList of users media without stop words: ')
for doc in documents:
    print(doc)
