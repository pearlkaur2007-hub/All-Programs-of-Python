#11. Write a Python program to create a set and iterate through it to print all unique elements.
s=[]
n=int(input('Enter no. of elements: '))
for ele in range(n):
    ele=int(input('Enter element: '))
    s.append(ele)
s=set(s)
print()
print('Original set', s)
print()
print('The unique elements are as follows:')
for i in s:
    print(i)