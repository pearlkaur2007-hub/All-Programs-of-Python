#12. Write a recursive function to perform binary search on a sorted list.
l1=[]
n=int(input("Enter no of elements in sorted list:"))
for ele in range(n):
    ele=int(input("Enter element:"))
    l1.append(ele)
target=int(input("Enter number to be searched:"))

def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, right, target)
    else:
        return binary_search(arr, left, mid - 1, target)
print('The index of element searched in list: ',binary_search(l1,0,n-1,target))