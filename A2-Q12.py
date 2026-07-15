#12. Write a Python program to perform union, intersection, and difference operations on two 
#sets.
s1=[]
s2=[]
n1=int(input('Enter no. of elements in n1: '))
n2=int(input('Enter no. of elements in n2: '))
for ele in range(n1):
  ele=int(input('Enter element: '))
  s1.append(ele)
for el in range(n2):
  el=int(input('Enter element: '))
  s2.append(el)
s1=set(s1)
s2=set(s2)
def union(s1,s2):
  print('Union: ',s1.union(s2))
def intersection(s1,s2):
  print('Intersection: ',s1.intersection(s2))
def difference(s1,s2):
  print('Difference: ',s1.difference(s2))
def symmetric_difference(s1,s2):
  print('Symmetric Difference: ',s1.symmetric_difference(s2))
union(s1,s2)
intersection(s1,s2)
difference(s1,s2)
symmetric_difference(s1,s2)