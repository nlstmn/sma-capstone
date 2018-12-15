import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
import multiprocessing
from gensim.utils import simple_preprocess


# Yields tagged documents matrix from 2D matrix of all users or brands' sma_data
# data_matrix = data.retrieve_sma_data(root_dir, user_type)
def create_tagged_document(data_matrix):
    for i, document in enumerate(data_matrix):
    #   user_data = document[1] + document[2]
        user_data = document[1]
        list_of_words = simple_preprocess(user_data)
        yield gensim.models.doc2vec.TaggedDocument(list_of_words, [document[0]])


# Trains data using Doc2Vec module and returns trained model instance
# vector_size: dimensionality of the feature vectors
# min_count: ignores all words with total frequency lower than this
# epochs: number of iterations (epochs) over the corpus
# dm: defines the training algorithm
# If dm=1, ‘distributed memory’ (PV-DM) is used,
# otherwise, distributed bag of words (PV-DBOW) is employed
def train_data(tagged_documents, vector_size, min_count, epochs, dm):
    cores = multiprocessing.cpu_count()
    model = gensim.models.doc2vec.Doc2Vec(vector_size=vector_size, min_count=min_count, epochs=epochs, dm=dm, workers=cores)
    model.build_vocab(tagged_documents)
    model.train(tagged_documents, total_examples=model.corpus_count, epochs=model.epochs)

    return model


# Returns iferred vector of an user by using user data (data.retrieve_user_sma_data) from given trained model
def get_user_vector(user_data, model):
 #   data = user_data[1] + user_data[2]
    data = user_data[1]
    list_of_words = simple_preprocess(data)

    return model.infer_vector(list_of_words)


# Loads trained model and returns it
# Model Type can be 'user' or 'brand'
def get_model(model_type):
    return gensim.models.doc2vec.Doc2Vec.load('brinfluence/lib/models/' + model_type + '_model')
