import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import re
import csv

f=open(r'C:\\Users\\User\\Desktop\\Tamil Madurai.txt',encoding="utf-8") 
content=f.read()

def SpecialCharacterRemoval(content):
    result = re.sub(r"['(',')'@\'?\.$%_]", "", content)
    return(result)
 
        
def Output(Out):
    with open('result.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for key,value in Out.items():
            tmp=[key,value]
            writer.writerow(tmp)    


def Findgrams(file,num):
    d=SpecialCharacterRemoval(file)
    token = nltk.word_tokenize(d)
    Ngrams= ngrams(token,num)
    Out=Counter(Ngrams)
    Output(Out)
    

Findgrams(content,6)


            
          
            