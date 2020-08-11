from bs4 import BeautifulSoup as bs
import os

content = []
with open("test.xml", "r") as file:
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = bs(content, "lxml")
#print(bs_content)

both = bs_content.find_all(['docno', 'text'])
doc = bs_content.find_all('docno')
#print(both)
#result1 = bs_content.find("text")

#print(both[2])
b = ".txt"
for i, p in enumerate(both):
    if (i % 2) == 0:
        f = open(os.path.join("Extracted Docs", (both[i].text + b)), "w+")
        f.write(both[i+1].text)
        f.close
