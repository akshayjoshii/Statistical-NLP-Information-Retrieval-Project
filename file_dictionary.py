import os

def populateDocumentEvidenceList(directory):
    doc_dictionary = {}
    for path, dirs, files in os.walk(directory):
        folders = path.split(os.sep)

        for dir in dirs:
            inner_path = path + '/' + dir
            populateDocumentEvidenceList(inner_path)

        for i, file in enumerate(files):
            if file.endswith(".txt"):
                doc_dictionary[i] = file
    return doc_dictionary

path = os.path.join("Extracted Docs")
result_dict = populateDocumentEvidenceList(path)
#print(list(result_dict.items())[:20])


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




