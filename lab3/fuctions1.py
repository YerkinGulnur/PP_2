#ex1
a = int(input())
def ounce(a : int):
    b = a * 28.3495231
    return b 
print (ounce(a))
#ex2
F = int(input())
def tem(a : int):
    C = (5/9) * (a - 32)
    return C 
print (tem(F))
#ex3
numlegs=94
numheads=35
import math
def solve(numlegs,numheads):
    rabbits=(numlegs/2)-numheads
    chickens=numheads-rabbits
    print(rabbits, " ", chickens)
solve(numlegs,numheads)
#ex4
def filter_prime(number):
    for i in number: 
        if i>1: 
            for j in range(2, i): 
                if(i%j)==0: 
                    break 
            else: 
                print(i)
prime=[int(i) for i in input().split()]
filter_prime(prime)
#ex5
def toString(List):
    return ''.join(List)
def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i]=a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i]=a[i], a[l]
s=str(input())
n=len(s)
a=list(s)
permute(a, 0, n)
#ex6
text=input()
def to_reverse(text):
    return ' '.join(text.split()[::-1])
result=to_reverse(text)
print(result)
#ex7
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i:i+2]==[3,3]:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
#ex8
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i]==0:
            for x in range(i+1,len(nums)):
                if nums[x]==0:
                    for y in range(x+1,len(nums)):
                        if nums[y]==7:
                            return True
                else:
                    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
#ex9
r=int(input())
def radius(a:float):
    pi=3.14159
    vl=4/3*pi*pow(a,3)
    print(vl)
radius(r)
 #ex10
def unique(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
l=list(map(int, input().split()))
print(unique(l))
#ex11
def name(s):
        t=s[::-1]
        if t==s:
            return True
        else:
            return False
print(name(input()))
#ex12
def histogram(a):
    for n in a:
        res = ''
        size = n
        while( size > 0 ):
          res += '*'
          size= size - 1
        print(res)

histogram([4,9,7])
#ex13
import random
name=input("Hello! What is your name?\n")
print("Well, %s, I am thinking of a number between 1 and 20." % name)
sol=random.randint(1, 20)
n=int(input("Take a guess.\n"))
cnt=1
while n!=sol:
    if n<sol:
        print("Your guess is too low.")
    elif n>sol:
        print("Your guess is too high.")
    n=int(input("Take a guess.\n"))
    cnt+=1
print("Good job, %s! You guessed my number in %d guesses!" % (name, cnt))


