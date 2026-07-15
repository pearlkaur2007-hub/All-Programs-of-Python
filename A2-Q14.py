#14. Write a Python program to swap keys and values in a dictionary.
l1=[]
n=int(input("Enter no of keys/values in dict: "))
for i in range(n):
    i=input("Enter key: ")
    l1.append(i)
l2=[]
for i in range(n):
    i=input("Enter value: ")
    l2.append(i)
d=dict(zip(l1,l2))
print("original dict: ", d)
new_d=dict(zip(l2,l1))
print("New dict: ",new_d)