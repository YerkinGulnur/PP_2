#ex1
#ex1
n=[int(i) for i in input().split()]
res=1
for i in n:
    res*=i
print(res)
#ex2
s=str(input())
cntc=0
cnts=0
for i in s:
    if i.isupper():
        cntc+=1
    else:
        cnts+=1
print(cntc)
print(cnts)
#ex3
a = input()
if a == ''.join(reversed(a)):
    print("Is Palindrom")
else:
    print("No Palindrom")
#ex4
import math, time
a = int(input())
mill = int(input())
time.sleep(mill/1000)
print("Square root of",a,"after",mill,"miliseconds is" ,math.sqrt(a))
#ex5
def all_true(tup):
    return all(tup)
my_tup=(True,True,True)
print(all_true(my_tup))