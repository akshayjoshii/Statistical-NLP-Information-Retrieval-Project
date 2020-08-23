# from regex_tokenize import RegexTokenizer
#
# text = """Bill 1.4 Gates. don't mid-90's ank-agr
#     ank
#     a   b
#     """
# obj = RegexTokenizer()
# t = obj.get_tokens(text)
# print(t)
#

# s = 'ank.txt'
# a = s.strip('.txt')
# b = a + '_1.txt'
# print(b)
# sentes = []
# top_50_sentences = [['a', 'bid', 'by', 'the'], ['executive', 'with', 'qintex']]
# for sentence in top_50_sentences:
#     sentos = " ".join(sentence)
#     sentes.append(sentos)
# print(sentes)
#
# def get_precision_sentences(top50_sents, patterns_query, precise_docs_bm25):
#     for sent in top50_sents:
#         result = precisionAtK(sent, patterns_query)
#         if result == True:
#             precise_docs_bm25.append(1)
#     return precise_docs_bm25
#
#
# if isBM25 == True:
#     i = 1
#     for pattern in query_to_pattern_map:
#         result = bool(re.findall(pattern, sent, flags = re.IGNORECASE))
#         if result == True:
#             return True
# input_document.close()
# return False
#

s = ['Extracted Docs/ LA010189-0045 .txt', 'Extracted Docs/FT941-11037.txt']
for a in s:
    b = a.replace('Extracted Docs', 'Unprocessed_Docs')
    print(b)
print(s)