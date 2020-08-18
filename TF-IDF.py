__author__ = "Akshay Joshi"
__email__ = "s8akjosh@stud.uni-saarland.de"

import math
import sys
import numpy as np

class TFIDF:
    def __init__(self):
        tf_idf = {}
        for i in range(N):
            tokens = processed_text[i]
            counter = Counter(tokens + processed_title[i])
            for token in np.unique(tokens):
                tf = counter[token]/words_count
                df = doc_freq(token)
                idf = np.log(N/(df+1))
                tf_idf[doc, token] = tf*idf
    
    def termFrequency(self, term, docs):
        pass

    def inverseDocumentFrequency(self, term, totaldocs):
        pass

    def queryTerms(self, terms):
        pass

    def cosineSimilarity(self, query, docs):
        pass

    def precision(self, query, similarity_vals):
        pass

    def meanPrecision(self, queries, similarity_vals):
        pass


if __name__ == "__main__":
    pass
