#ex1
import re 
a = str(input())
b = re.search("ab*", a)
if b:
    print("yes")
else:
    print("no")
#ex2
import re
a = input()
if re.search('ab{2,3}', a):
    print("Find")
else:
    print("not found")
#ex3
import re
a = input()
b = re.findall("[^A-Z]\w+_\w+", a)
print(b)
#ex4
import re
a = input()
b = re.findall("[A-Z]+[a-z]+$", a)
print(b)
#ex5
import re
a = input()
b = re.findall("a.*b$", a)
print(b)
#ex6
import re
a = input()
b = re.sub("[\s,.]", ":", a)
print(b)
#ex7
import re
text=input()
pattern=r'[a-z][^_]*'
ls=re.findall(pattern, text)
res=" "
for i in ls:
    res+=i.capitalize()
print(res)
#ex8
import re
a = input()
b = re.findall("[A-Z][^A-Z]*", a)
print(b)
#ex9
import re
a = input()
b = re.findall("[A-Z][^A-Z]*", a)
c = " ".join(b)
print(c)
#ex10
import re
text=input()
ls=re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
res=""
for i in ls:
    res+=i.lower()
print(res)