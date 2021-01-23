import regex as re
from collections import Counter
import csv
file=open(r'C:\\Users\\User\\Desktop\\Tamil Madurai.txt',encoding="utf-8") 
content=file.read()
#print(content)
result = re.sub(r"'(',')',[,@\'?\.$%_]", "", content)
x = re.findall(r"\w+", result)
x1=re.findall(r"\b\w+\s\w+",result,overlapped=True)
x2=re.findall(r"\b\w+\s\w+\s\w+",result,overlapped=True)
c1=Counter(x)

with open('unigram.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for key,value in c1.items():
        tmp=[key,value]
        writer.writerow(tmp)
    
 
c2= Counter(x1)

with open('bigram.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for key,value in c2.items():
        tmp=[key,value]
        writer.writerow(tmp)
        
file.close()        

c3=Counter(x2)

with open('trigram.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for key,value in c3.items():
        tmp=[key,value]
        writer.writerow(tmp)

