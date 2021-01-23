import nltk
import bs4 as bs
import urllib.request
import re
from nltk.util import ngrams
from collections import Counter

file = urllib.request.urlopen('https://en.wikipedia.org/wiki/Life')
file = file.read()

content = bs.BeautifulSoup(file, 'lxml')
paragraphs = content.find_all('p')
text = ''

for para in paragraphs:
    text += para.text


def SpecialCharacterRemoval(text):
    result = re.sub(r"['[['(',')'@\'?\.:;$%_]", "", text)
    result = result.replace(']', r"")
    return(result)
 

def Findgrams(articles,num):
    d=SpecialCharacterRemoval(articles)
    token = nltk.word_tokenize(d)
    Ngrams= ngrams(token,num)
    X=Counter(Ngrams)
    print("Maximum Repeated Pairs",X.most_common(10))
    


Findgrams(text,1)  
Findgrams(text,2)
