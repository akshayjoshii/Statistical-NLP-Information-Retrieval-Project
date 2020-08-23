import nltk
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
import numpy as np


class BM25Rank():
    def __init__(self, scores):
        self.scores = scores
        self.characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>``'`"
        self.doc_corpus = []
        self.sentence_corpus = []
        self.no_of_docs_reqd = 10
        self.final_rank = {}
        self.bm25_rank_dict = {}
        self.top50_rank_list = {}

    def tokenize(self, document):
        terms = document.lower().split()
        return [term.strip(self.characters) for term in terms]

    def write_to_dict(self, bm25rank=None):
        for index, item in enumerate(self.scores):
            if item not in self.final_rank:
                self.final_rank[item] = {'previous_ranking': index, 'bm25_ranking': bm25rank.index(index)}
                self.bm25_rank_dict[item] = bm25rank.index(index)
        print(self.final_rank)

    def top50_rank(self):
        scores = sorted([(key, value) for key, value in self.bm25_rank_dict.items()],
                        key=lambda x: x[1], reverse=False)[:self.no_of_docs_reqd]
        print(scores)
        return scores

    def get_doc_rank(self):
        for id in self.scores:
            f = open(id, 'r')
            document = f.read()
            f.close()
            doc_terms = self.tokenize(document)
            self.doc_corpus.append(doc_terms)
        bm25 = BM25Okapi(self.doc_corpus)
        query = "what debts did qintex group leave ?"
        tokenized_query = self.tokenize(query)
        doc_scores = bm25.get_scores(tokenized_query)
        print(doc_scores)
        doc_scores_sorted = np.argsort(doc_scores)[::-1]
        # top_n = bm25.get_top_n(tokenized_query, self.doc_corpus, n=1)
        print(doc_scores_sorted)
        self.write_to_dict(doc_scores_sorted.tolist())
        self.top50_rank_list = self.top50_rank()
        return self.top50_rank_list

    def get_sentence_rank(self):
        for id, rank in self.top50_rank_list:
            f = open(id, 'r')
            document = f.read()
            f.close()
            sentences = nltk.sent_tokenize(document)  # this gives us a list of sentences
            # now loop over each sentence and tokenize it separately
            sentence_terms = ''
            for sentence in sentences:
                sentence_terms = self.tokenize(sentence)
            self.sentence_corpus.append(sentence_terms)
        bm25 = BM25Okapi(self.sentence_corpus)

        query = "what debts did qintex group leave ?"
        tokenized_query = self.tokenize(query)

        sent_scores = bm25.get_scores(tokenized_query)
        print(sent_scores)
        sent_scores_sorted = np.argsort(sent_scores)[::-1][:self.no_of_docs_reqd]
        top_50_sentences = bm25.get_top_n(tokenized_query, self.sentence_corpus, n=self.no_of_docs_reqd)
        for item in top_50_sentences:
            print(item)
        # print(top_50_sentences)
        # print(doc_scores_sorted)
        # self.write_to_dict(doc_scores_sorted.tolist())
        # self.top50_rank_list = self.top50_rank()
        # return self.top50_rank_list

# Driver code
if __name__ == "__main__":
    score = ['Extracted Docs/ LA102189-0132 .txt', 'Extracted Docs/ LA060690-0106 .txt', 'Extracted Docs/ LA112189-0092 .txt', 'Extracted Docs/ LA102789-0129 .txt', 'Extracted Docs/ LA112189-0145 .txt', 'Extracted Docs/ LA102489-0083 .txt', 'Extracted Docs/ LA053089-0114 .txt', 'Extracted Docs/ LA101989-0172 .txt', 'Extracted Docs/ LA102189-0131 .txt', 'Extracted Docs/ LA110389-0124 .txt']
    obj = BM25Rank(score)
    top50_docs = obj.get_doc_rank()
    obj.get_sentence_rank()

