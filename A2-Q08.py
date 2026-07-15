#8. Write a Python program to remove duplicate elements from a list without using the set() 
#function.
l1=[]
n=int(input('Enter no. of elements in list: '))
for ele in range(n):
    ele=int(input('Enter element: '))
    l1.append(ele)
print("Original List: ", l1)
l2=[]
for ele in l1:
    if ele not in l2:
        l2.append(ele)
print("New List: ",l2)