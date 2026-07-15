#5. Write a Python program to traverse a tuple and count how many elements are even
#numbers.
tup=[]
n=int(input('Enter no of elements in tuple: '))
for ele in range(n):
    ele=int(input('Enter an element: '))
    tup.append(ele)
tup1=tuple(tup)
print(tup1)
c=0
#Transversing a Tuple
for ele in tup1:
    if ele%2==0:
        c+=1
print('The no. of even number/s in tuple : ', c)
