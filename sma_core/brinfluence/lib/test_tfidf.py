from gensim import corpora
from gensim import models
from gensim.utils import simple_preprocess
import numpy as np

documents = ["I love photograpy. Photography is art. Taking photos is my life.",
             "I am interested in something else, I like cars",
             "I am in love with photography. Photography is my life and I enjoy taking photos"]

# Create the Dictionary and Corpus
mydict = corpora.Dictionary([simple_preprocess(line) for line in documents])
corpus = [mydict.doc2bow(simple_preprocess(line)) for line in documents]

# Show the Word Weights in Corpus
for doc in corpus:
    print([[mydict[id], freq] for id, freq in doc])

# Create the TF-IDF model
tfidf = models.TfidfModel(corpus, smartirs='ntc')

print("\n")
# Show the TF-IDF weights
for doc in tfidf[corpus]:
    print([[mydict[id], np.around(freq, decimals=2)] for id, freq in doc])
