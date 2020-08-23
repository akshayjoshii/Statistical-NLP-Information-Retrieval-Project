__author__ = "Ankit Agrawal"
__email__ = "s8anagra@stud.uni-saarland.de"


import string
import re


class RegexTokenizer:
    def __init__(self):
        self.text = ''
        punctuation_tokens = ['..', '...', ',', ';', ':', '(', ')', '"', '\'', '[', ']',
                              '{', '}', '?', '!', '-', '–', '+', '*', '--', '\'\'', '``', ',,,', '…', '’', '...', '`']
        punctuation2 = list(string.punctuation)
        self.punt = punctuation2 + punctuation_tokens
        self.regex_str = [
            r"(?:(?:[a-z]|[0-9])+['\-_]+(?:[a-z]|[0-9])+['\-_]*(?:[a-z]|[0-9])*)", # words with - and '
            r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
            r'(?:[\w_]+)',  # other words
            r'(?:\S)'  # anything else
        ]
        self.tokens_re = re.compile(r'(' + '|'.join(self.regex_str) + ')', re.VERBOSE | re.IGNORECASE)
        self.lowercase = True

    def tokenize(self):
        return self.tokens_re.findall(self.text)

    def preprocess(self):
        tokens = self.tokenize()
        if self.lowercase:
            tokens = [token.lower() for token in tokens]
        return tokens

    def get_tokens(self, text, lowercase=True):
        self.text = text
        self.lowercase = lowercase
        final_tokens = [term for term in self.preprocess() if term not in self.punt]
        return final_tokens

