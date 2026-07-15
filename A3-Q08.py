#8. Write a recursive function to generate all permutations of a string.  
def perm(string1,i):
    if len(string1)==1:
        return string1
    for char in range(len(string1)):
        char=string1[i]
        rem=string1[i+1:]+string1[:i]
    perm(string1,i+1)
string1=str(input("Enter a string: "))
i=0
perm(string1[0])