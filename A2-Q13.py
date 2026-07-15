#13. Write a Python program to iterate through a dictionary and print all keys and their 
#corresponding values.
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
for key,value in d.items():
    print(key,':',value)