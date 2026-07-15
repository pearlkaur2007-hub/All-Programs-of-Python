#3. Write a Python program to find the maximum and minimum elements in a list.
l1=[]
n=int(input('Enter no of elements in list: '))
for i in range(n):
    ele=int(input('Enter element: ')) #input of element
    l1.append(ele)                    #adding to list
max=l1[0]                             #assuming max
min=l1[0]                             #assuming min
for el in l1:
    if(el>max):                       
        max=el
    if(el<min):
        min=el
print('The minimum and maximum element in the list is: ',min,'& ', max)