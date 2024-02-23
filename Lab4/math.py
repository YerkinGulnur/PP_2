#ex1
import cmath
degr = int(input('Input degree: '))
rad = (cmath.pi / 180) * degr

print("Output radian: " + str(rad))
#ex2
a = int(input('Height: '))
b = int(input('Base, first value: '))
c = int(input('base, second value: '))

area = 0.5 * a * (b + c)

print(area)
#ex3
import cmath as matesha
n = int(input())
a = int(input())

s = n * (a**2)/4 * matesha.tan(matesha.pi/n)
print(s)
#ex4
a=float(input('Length of base: '))
b=float(input('Height of parallelogram: '))
s=a*b
print('Expected Output:', s)