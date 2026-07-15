#17. Write a Python program to print elements of a list along with their indices using the 
#enumerate() function.

l1=[]
n=int(input('Enter no. of elements in list: '))
for ele in range(n):
    ele=int(input('Enter element: '))
    l1.append(ele)
print(list(enumerate(l1,start=0)))
