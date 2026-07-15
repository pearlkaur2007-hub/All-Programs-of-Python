#9. Write a Python program to reverse a list using iteration without using built-in functions. 
l1=[]
n=int(input('Enter no. of elements: '))
for ele in range(n):
    ele=int(input('Enter the element: '))
    l1.append(ele)
left=l1[0]
right=l1[n-1]
l2=[]
el=n-1
for i in range(n):
    i=l1[el-i]
    l2.append(i)
print('Original List: ', l1)
print('New List: ',l2)