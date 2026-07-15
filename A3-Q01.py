#1. Write a recursive function to check whether a string is a palindrome.  
def palin(n1):
    if len(n1)<=1:
        return True
    if n1[0]!=n1[-1]:
        return False
    return palin(n1[1:-1])
n1=str(input('Enter the string: '))
n=n1.lower()

if palin(n):
    print('It is a Palindrome string.')
else:
    print('Not a Palindrome string.')