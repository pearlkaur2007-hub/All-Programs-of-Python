#23. Write a Python program to group a list of strings into anagrams (e.g., ["eat", "tea", "tan"]).
l1=[]
n=int(input("Enter no of elements: "))
for i in range(n):
    i=str(input("Enter string: "))
    l1.append(i)
print("Original: ",l1)
l2=[]
for i in range(n):
    for j in range(i+1, n):
        if sorted(l1[i]) == sorted(l1[j]):
            print("Anagram found:", l1[i], l1[j])
            l2.append(l1[i])
            l2.append(l1[j])
print("Anagram:",l2)