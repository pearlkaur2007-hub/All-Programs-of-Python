#25. Write a Python program to merge two sorted lists into a single sorted list without using 
#built-in sorting functions.
l1=[]
n=int(input("Enter no of elements in list 1: "))
print("The elements entered should be in sorted order.")
for i in range(n):
    i=int(input("Enter element: "))
    l1.append(i)
l2=[]
m=int(input("Enter no of elements in list 2: "))
print("The elements entered should be in sorted order.")
for j in range(m):
    j=int(input("Enter element:"))
    l2.append(j)
print("List 1: ",l1)
print("List 2:",l2)
i=0
j=0
sorted_list=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        sorted_list.append(l1[i])
        i+=1
    else:
        sorted_list.append(l2[j])
        j+=1
while i < len(l1):
    sorted_list.append(l1[i])
    i += 1
while j < len(l2):
    sorted_list.append(l2[j])
    j += 1
print("Merged list:", sorted_list)