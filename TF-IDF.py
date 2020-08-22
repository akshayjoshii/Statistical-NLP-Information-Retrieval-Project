__author__ = "Akshay Joshi"
__email__ = "s8akjosh@stud.uni-saarland.de"

import math
import sys
import os
import numpy as np
from collections import defaultdict
from functools import reduce

class TFIDF:
    def __init__(self):
        self.word_dict = set()
        self.postings = defaultdict(dict)
        self.document_frequency = defaultdict(int)
        self.length = defaultdict(float)
        self.characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>"

    def populateDocumentEvidenceList(self, directory):
        doc_dictionary = {}
        for path, dirs, files in os.walk(directory):
            folders = path.split(os.sep)

            # Parse all the sub directories in the root directory
            for dir in dirs:
                inner_path = path + '/' + dir
                populateDocumentEvidenceList(inner_path)

            # Parse all the files in the directories list
            for i, file in enumerate(files):
                if file.endswith(".txt"):
                    doc_dictionary[i] = file
        return doc_dictionary
    

    def initialize_terms_and_postings(self):
        """Reads in each document in doc_dictionary, splits it into a
        list of terms (i.e., tokenizes it), adds new terms to the global
        dictionary, and adds the document to the posting list for each
        term, with value equal to the frequency of the term in the
        document."""
        global self.word_dict, self.postings
        for id in doc_dictionary:
            f = open(doc_dictionary[id],'r')
            document = f.read()
            f.close()
            terms = tokenize(document)
            unique_terms = set(terms)
            dictionary = dictionary.union(unique_terms)
            for term in unique_terms:
                postings[term][id] = terms.count(term) # the value is the
                                                    # frequency of the
                                                    # term in the
                                                    # document

    def tokenize(self, document):
        """Returns a list whose elements are the separate terms in
        document.  Something of a hack, but for the simple documents we're
        using, it's okay.  Note that we case-fold when we tokenize, i.e.,
        we lowercase everything."""
        terms = document.lower().split()
        return [term.strip(self.characters) for term in terms]

    def initialize_document_frequencies(self):
        """For each term in the dictionary, count the number of documents
        it appears in, and store the value in document_frequncy[term]."""
        global document_frequency
        for term in dictionary:
            document_frequency[term] = len(postings[term])

    def initialize_lengths(self):
        """Computes the length for each document."""
        global length
        for id in doc_dictionary:
            l = 0
            for term in dictionary:
                l += imp(term,id)**2
            length[id] = math.sqrt(l)

    def imp(self, term,id):
        """Returns the importance of term in document id.  If the term
        isn't in the document, then return 0."""
        if id in postings[term]:
            return postings[term][id]*inverse_document_frequency(term)
        else:
            return 0.0

    def inverse_document_frequency(self, term, corpus_length):
        """Returns the inverse document frequency of term.  Note that if
        term isn't in the dictionary then it returns 0, by convention."""
        if term in self.word_dict:
            return math.log(corpus_length/document_frequency[term],2)
        else:
            return 0.0

    def do_search(self, corpus_length):
        """Asks the user what they would like to search for, and returns a
        list of relevant documents, in decreasing order of cosine
        similarity."""
        corpus_length = corpus_length
        query = self.tokenize(input("Enter Query: "))
        if query == []:
            sys.exit()
        # find document ids containing all query terms.  Works by
        # intersecting the posting lists for all query terms.
        relevant_document_ids = self.intersection(
                [set(self.postings[term].keys()) for term in query])
        if not relevant_document_ids:
            print ("No documents matched all query terms")
        else:
            scores = sorted([(id,self.similarity(query, id, corpus_length))
                            for id in relevant_document_ids],
                            key=lambda x: x[1],
                            reverse=True)
            print ("Score: filename")
            for (id,score) in scores:
                print(str(score)+": "+doc_dictionary[id])

    def intersection(self, sets):
        """Returns the intersection of all sets in the list sets. Requires
        that the list sets contains at least one element, otherwise it
        raises an error."""
        return reduce(set.intersection, [s for s in sets])

    def similarity(self, query, id, corpus_length):
        """Returns the cosine similarity between query and document id.
        Note that we don't bother dividing by the length of the query
        vector, since this doesn't make any difference to the ordering of
        search results."""
        similarity = 0.0
        for term in query:
            if term in self.word_dict:
                similarity += self.inverse_document_frequency(term, corpus_lenth)*self.imp(term,id)
        similarity = similarity / self.length[id]
        return similarity



if __name__ == "__main__":
    path = os.path.join("Extracted Docs")
    a = TFIDF()
    doc_dictionary = a.populateDocumentEvidenceList(path)
    #print(list(result_dict.items())[:20])
    corpus_length = len(doc_dictionary)
    print(f"Total document evidences populated in the dictionary: {corpus_length}")
    #while True:
        #a.do_search(corpus_length)


