#ex1
def gen(n,k=1):
    while k<=n:
        yield k**2
        k+=1
n=int(input())
g=gen(n)
for i in g:
    print(i)
#ex2
a=int(input())
def even(a):
    for i in range(a+1):
        if (i%2==0):
            yield i
for i in even(a):
    print(i,end=' , ')
#ex3
a=int(input())
def div(a):
    for i in range(a+1):
        if(i%3==0) and (i%4==0):
            yield i
for i in div(a):
    print(i)
#ex4
a=int(input())
b=int(input())
for i in range(a,b+1):
    print(i*i)
#ex5
def generator(n):
    while n>=0:
        yield n
        n-=1
n=int(input())
g=generator(n)
for i in g:
    print(i,end=' ')