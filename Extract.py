__author__ = "Akshay Joshi"
__email__ = "s8akjosh@stud.uni-saarland.de"

import os
import string
import sys
import unicodedata
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup as bs

class Extract:
    
    # Initializing class attributes
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.token_rule = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))
        self.extension = ".txt"
        self.path = "Extracted Docs"
        self.delete_list = ["<top>", "</top>", "<desc> Description:", "<num> Number: "]


    def retrieveDocumentEvidences(self, xmlfile):
        xml_content = []
        print("\n[INFO] Please be patient, parsing huge xml file!")
        with open(xmlfile, "r") as file:
            xml_content = file.readlines()

            # Combine the lines in the list into a string
            xml_content = "".join(xml_content)

            # Using lxml module to force parse xml docs instead of using HTML module from BS4
            bs_content = bs(xml_content, "lxml")

        # Extracting contents within 'DOCNO' & 'TEXT' html tags
        tag_contents = bs_content.find_all(['docno', 'text'])
        
        #for t in tqdm(range(len(tag_contents)), desc = "Document parse progress: "):
        for i, p in enumerate(tag_contents):
            if (i % 2) == 0:
                f = open(os.path.join(self.path, (tag_contents[i].text + self.extension)), "w+")
                raw_file_content = tag_contents[i+1].text
                # Pre-processing raw text before tokenizing to preven't corruption/elimination of words such as 'can't' or 'english-spoken'
                processed_file_content = raw_file_content.translate(self.token_rule)
                tokens = word_tokenize(processed_file_content)
                tokens_without_sw = [word.lower() for word in tokens if not word in self.stop_words]
                f.write(" ".join(tokens_without_sw))
                f.close
        print("\n[INFO] Document evidence parsing complete")
        print(f"\nDocuments saved in directory: {self.path}")


    # Function to parse the unstructered test_question.txt file
    def extractQueries(self, intxt, outtxt):
        processed_queries = []
        with open(intxt, "r") as inp:
            for line in inp:
                for word in self.delete_list:
                    line = line.replace(word, "")
                processed_queries.append(line)
        inp.close

        with open(outtxt, "w+") as oup:
            for line in processed_queries:
                if line.strip():
                    line = line.translate(self.token_rule)
                    oup.write(line.lower())
        oup.close 
        print("\n[INFO] Parsing Test Questions file complete!")
        print(f"\nTest Questions file saved as: {outtxt}")

    
# Driver code
if __name__ == "__main__":
        # Create separate docs by extracting info inside <text> tags from xml
        e = Extract()
        e.retrieveDocumentEvidences("trec_documents.xml")
        e.extractQueries("test_questions.txt", "extracted_test_questions.txt")
