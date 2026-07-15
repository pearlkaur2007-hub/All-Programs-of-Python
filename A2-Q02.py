#2. Write a Python program to find the sum of all elements in a given list.
l1=[]
n=int(input('Enter no of elements in list: '))
sum=0
for i in range(n):
    ele=int(input('Enter element: ')) #input of element
    l1.append(ele)                    #adding to list
    sum+=ele                          #sum of each element
print('The sum of all the elements in the list is ', sum)