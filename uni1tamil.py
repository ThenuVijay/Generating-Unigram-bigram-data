import regex as re
from collections import Counter
import csv
file=open(r'C:\\Users\\User\\Desktop\\new1.txt',encoding="utf-8") 
content=file.read()
#print(content)
result = re.sub(r"[,@\'?\.$%_]", "", content)
x = re.findall(r"\w+", result)
x1=re.findall(r"\b\w+\s\w+",result,overlapped=True)
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


