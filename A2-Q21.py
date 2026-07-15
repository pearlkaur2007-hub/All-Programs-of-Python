#21. Write a Python program to find two numbers in a list that add up to a given target value 
#(Two Sum problem).
l1=[]
n=int(input("Enter no. of elements in list: "))
for ele in range(n):
    ele=int(input("Enter element: "))
    l1.append(ele)
print("Original List: ", l1)
target=int(input("Enter Target: "))
for ele in range(n):
    for j in range(ele+1,n):
        if l1[ele]+l1[j]==target:
            print(l1[ele],l1[j])
