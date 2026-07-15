#18. Write a Python program to combine two lists into a dictionary using the zip() function.
l1=[]
n=int(input("No. of keys/values in dict: "))
for i in range(n):
    i=input("Enter keys: ")
    l1.append(i)
l2=[]
for i in range(n):
    i=input("Enter value: ")
    l2.append(i)
d=dict(zip(l1,l2))
print(d)