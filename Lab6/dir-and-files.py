#ex1
import os
# path='/Users/erkin.gulnur/Desktop/PP2/Lab6'
dir, file, all = 0, 0, 0
put=os.getcwd()
print("DIR:")
for target in os.listdir('.'):
    if os.path.isdir(os.path.join(target)): 
        dir+=1  
        print(target)
print('FILE:')
for target in os.listdir('.'):
    if os.path.isfile(os.path.join(target)):
        file+=1
        print(target)

print("ALL:")
for target in os.listdir('.'):
    all+=1
    print(target)
    
print(dir)
print(file)
print(all)
#ex2
import os
print('Exist:', os.access('Lab6/gulnur.txt', os.F_OK))
print('Readable:', os.access('Lab6/gulnur.txt', os.R_OK))
print('Writable:', os.access('Lab6/gulnur.txt', os.W_OK))
print('Executable:', os.access('Lab6/gulnur.txt', os.X_OK))
#ex3
import os
path='Lab6/dir-and-files.py'
print("Test a path exists or not:")
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDirectory name of the path:")
print(os.path.dirname(path))
#ex4
import os
a = open('Lab6/dir-and-files.py')
b = a.read()
c = b.split('\n')
print(len(c))
#ex5
color=['red', 'green', 'black',"purple"]
with open('Lab6/gulnur.txt', 'w') as f:
    for i in color:
        f.write(i+'\n')
text=open('Lab6/gulnur.txt', 'r')
print(text.read())
#ex6
import os
import string
for i in string.ascii_uppercase:
    with open(i+'.txt', 'w')as f:
        f.writelines(i)
 #ex7
with open('Lab6/gulnur.txt', 'r') as f:
    with open('Lab6/1.txt', 'w') as f1:
        for line in f:
            f1.write(line)
#ex8
import os 
path='Lab6/gulnur.txt'
print(os.path.exists(path))
print(os.remove(path))