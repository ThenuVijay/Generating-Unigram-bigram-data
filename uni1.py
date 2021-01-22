import regex as re
from collections import Counter
file=open('C:\\Users\\User\\Desktop\\new.txt',"r") 
content=file.read()
result = re.sub(r"[,@\'?\.$%_]", "", content)
x = re.findall(r"\w+", result)
x1=re.findall(r"\b\w+\s\w+",result,overlapped=True)
print(Counter(x))
print(Counter(x1))





#File Content--->Tamil encoding has a long history with 8-bit extended ASCII called TSCII, TAM (Tamil Monolingual)/TAB (Tamil Bi-lingual) encodings of the late 80s and early 90s.

#Then enter Windows. Microsoft Windows with the Microsoft Word let some Tamil software vendors introduce font-based encodings. This probably is the most egregious of all Tamil encoding methods invented, IMO. Still this would show the books in fonts like Latha, Lohit etc. You needed the right font-map  with glyphs independent of encoding to read the text. Otherwise the text would end up garbled like a mish-mash of ‘?’ or []-(tofu block) characters.

#Finally the Tamil computing community, software ventors, members of INFITT (among others Mr. Chellappan of Palaniappa Brothers, Chennai, Prof. Ponnavaiko, and Dr. K. Kalyanasundaram of EPFL) sat down with the pioneering people at Unicode consortium and hashed out a chunk of the Unicode standards space for Tamil letters, which is what we have today. So now you know if Android, iOS and Windows support the Tamil text, it is most likely due to the benefit of years of work from this motely crew of genteel anonymous strangers. Thanks everyone!

#Now the web had matured since 1990s, and Unicode support by blogs, and input method editors (IME) on Linux, Windows and Mac enabled growth and exchange of Tamil content on the Internet. Unicode encoded in UTF-8 became the de-facto standard of the Tamil community online, despite diktats from Tamilnadu government, and other standards agencies which were left behind in the shadows of stand-alone computing world. Welcome Internet. Now change was not an option.