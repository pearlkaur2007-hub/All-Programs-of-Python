#24. Write a Python program to find the top K frequent elements in a list.
from collections import Counter 
l1=[]
n=int(input("Enter no of elements: "))
for i in range(n):
    i=int(input("Enter element: "))
    l1.append(i)
k=int(input("Enter value of k: "))
freq=Counter(l1)
most_common = freq.most_common(k)
result = [item[0] for item in most_common]
print("Top K frequent elements:", result)