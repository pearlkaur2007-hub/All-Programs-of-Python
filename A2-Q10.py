#10. Write a Python program to count the frequency of each element in a list.
l1=[]
n=int(input('Enter no. of elements in list: '))
for ele in range(n):
    ele=int(input('Enter element: '))
    l1.append(ele)
d={}
l2=[]
for ele in l1:
    if ele not in l2:
        d[ele]=1
        l2.append(ele)
    else:
        d[ele]+=1

print("Freq of elements are: ", d)
