from collections import defaultdict
import math
import sys
import os
import numpy as np
from collections import defaultdict
from functools import reduce

#path = os.path.join("test")
#document_filenames = populateDocumentEvidenceList(path)
#print(document_filenames)
dictionary = set()
postings = defaultdict(dict)
document_frequency = defaultdict(int)
length = defaultdict(float)

# The list of characters (mostly, punctuation) we want to strip out of
# terms in the document.
characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>``'`"

def populateDocumentEvidenceList(directory):
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
                doc_dictionary[i] = path+'/'+file
    return doc_dictionary


def initialize_terms_and_postings(document_filenames):
    global dictionary, postings
    #document_filenames = populateDocumentEvidenceList("test")
    for id in document_filenames:
        f = open(document_filenames[id],'r')
        document = f.read()
        f.close()
        terms = tokenize(document)
        unique_terms = set(terms)
        dictionary = dictionary.union(unique_terms)
        for term in unique_terms:
            postings[term][id] = terms.count(term)

def tokenize(document):
    terms = document.lower().split()
    return [term.strip(characters) for term in terms]

def initialize_document_frequencies():
    global document_frequency
    for term in dictionary:
        document_frequency[term] = len(postings[term])

def initialize_lengths(document_filenames):
    global length
    #document_filenames = populateDocumentEvidenceList("test")
    for id in document_filenames:
        l = 0
        for term in dictionary:
            l += imp(term,id, N)**2
        length[id] = math.sqrt(l)

def imp(term,id, N):
    if id in postings[term]:
        return postings[term][id]*inverse_document_frequency(term, N)
    else:
        return 0.0

def inverse_document_frequency(term, N):
    if term in dictionary:
        return math.log(N/document_frequency[term],2)
    else:
        return 0.0

def intersection(sets):
    return reduce(set.union, [s for s in sets])

def similarity(query,id, N):
    similarity = 0.0
    for term in query:
        if term in dictionary:
            similarity += inverse_document_frequency(term, N) * imp(term,id, N)
    similarity = similarity / length[id]
    return similarity


def do_search(document_filenames, N):
    #document_filenames = populateDocumentEvidenceList("test")
    query = tokenize(input("Search query >> "))
    if query == []:
        sys.exit()
    relevant_document_ids = intersection([set(postings[term].keys()) for term in query])
    scores = sorted([(id,similarity(query, id, N)) for id in relevant_document_ids], 
                    key=lambda x: x[1], reverse=True)[:50]
    print("Score: filename")
    for (id, score) in scores:
        print(str(score)+": "+document_filenames[id])


if __name__ == "__main__":
    path = "Extracted Docs"
    print("\n[INFO] Please be patient, building a massive postings list!")
    document_filenames = populateDocumentEvidenceList(path)
    N = len(document_filenames)
    initialize_terms_and_postings(document_filenames)
    initialize_document_frequencies()
    initialize_lengths(document_filenames)
    while True:
        do_search(document_filenames, N)