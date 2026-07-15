#7. Write a Python program to create a new list containing only even numbers from a given list.
l1=[]
n=int(input('Enter number of elements: '))
new_l1=[]
for ele in range(n):
    ele=int(input('Enter element: '))
    l1.append(ele)
l2=list(filter(lambda ele:ele%2==0, l1))
print('Original list', l1)
print('New list', l2)