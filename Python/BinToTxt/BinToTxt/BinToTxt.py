from gensim import corpora, models, similarities
from gensim.models.keyedvectors import KeyedVectors
print("..........StartConverting..........")
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
model.save_word2vec_format('GoogleNews-vectors-negative300.txt', binary=False)
print("..........DoneConverting..........")
