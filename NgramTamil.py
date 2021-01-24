import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import re
import csv

f=open(r'C:\\Users\\User\\Desktop\\Tamil Madurai.txt',encoding="utf-8") 
content=f.read()
f.close()

def SpecialCharacterRemoval(content):
    result = re.sub(r"['(',')'@\'?\.$%_]", "", content)
    return(result)

def writefile(num,Out):
    res="result"+str(num)+"."+"csv"
    print(res)
    with open(res, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for key,value in Out.items():
            tmp=[key,value]
            writer.writerow(tmp)  
    file.close()        


def Findgrams(file,num):
    d=SpecialCharacterRemoval(file)
    token = nltk.word_tokenize(d)
    Ngrams= ngrams(token,num)
    Out=Counter(Ngrams)
    writefile(num,Out)



    
Findgrams(content,1)
Findgrams(content,6)
            
          
            