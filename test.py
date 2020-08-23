import re
import string
s = """Bill 1.4 Gates. don't mid-90's ank-agr
    ank
    a   b
    """
characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>``'`"
aa = s.lower().split()
print(aa)
b = [a.strip(characters) for a in aa]
print(b)

punctuation_tokens = ['..', '...', ',', ';', ':', '(', ')', '"', '\'', '[', ']',
                      '{', '}', '?', '!', '-', '–', '+', '*', '--', '\'\'', '``', ',,,', '…', '’']
punctuation1 = '?!/;:()&+'
punctuation2 = list(string.punctuation)
stop = punctuation2 + punctuation_tokens + ['rt', 'via', '...', '`']

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    # r'<[^>]+>',  # HTML tags
    # r'(?:@[\w_]+)',  # @-mentions
    # r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    # r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    # r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    # r"(?:([a-z]|[0-9])[a-z0-9'\-_]+([a-z]|[0-9]))",
    # r"(?:([a-z]|[0-9])+['\-_]+([a-z]|[0-9])+['\-_]*([a-z]|[0-9])*)", #main
    r"(?:(?:[a-z]|[0-9])+['\-_]+(?:[a-z]|[0-9])+['\-_]*(?:[a-z]|[0-9])*)",
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers

    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(ss):
    return tokens_re.findall(ss)


def preprocess(ss, lowercase=False):
    tokens = tokenize(ss)
    print(tokens)
    if lowercase:
        tokens = [token.lower() for token in tokens]
    # print(tokens)
    return tokens


terms_stop = [term for term in preprocess(s) if term not in stop]
print(terms_stop)