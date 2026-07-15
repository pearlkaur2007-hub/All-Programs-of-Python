#7. Write a recursive function to find the maximum element in a list.
def maxi(l1,i,maxm):
    if l1[i]>maxm:
        maxm=l1[i]
    if i==n-1:
        print("The maximum element in the list is: ", maxm)
        return
    return maxi(l1,i+1,maxm)
l1=[]
n=int(input("Enter no of elements: "))
for i in range(n):
    i=int(input('Enter element: '))
    l1.append(i)
maxm=l1[0]
maxi(l1,0,maxm)
