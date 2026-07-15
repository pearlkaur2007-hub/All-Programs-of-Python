#16. Write a Python program to print numbers from 1 to 20 along with their squares using the 
#range() function.

for i in range(1,21):
    print(i,i*i)
result={}
for i in range(1,21):
    result[i]=i*i
print(result)