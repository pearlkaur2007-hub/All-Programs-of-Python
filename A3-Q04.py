#4. Write a recursive function to find the product of elements in a list.
def prod(l1,n):
    if n==0:
        return 1
    return l1[n-1]*prod(l1,n-1)
n=int(input("Enter the number of elements: "))
l1=[]
for i in range(n):
    i=int(input("Enter Element: "))
    l1.append(i)
print(l1)
print("The product of the numbers in the list: ", prod(l1,n))