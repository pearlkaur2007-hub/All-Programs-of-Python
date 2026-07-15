#1. Write a Python program to iterate over a list and print all its elements.

l1=[]
n=int(input('Enter number of elements in the list: ')) 
#input of elements in list
for i in range(n):
    ele=int(input('Enter element: '))
    l1.append(ele)
#printing all elements of list 
for i in range(n):
    print(l1[i], end=' ')