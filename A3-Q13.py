#13. Write a recursive function to check if a number is a palindrome without converting to string.
num=int(input("Enter a number:"))
temp=num
def palin(num,rev=0):
    if num==0:
        return rev
    digit=num%10
    rev=rev*10+digit
    num//=10
    return palin(num,rev)
if palin(num)==temp:
    print(num, 'is a palindrome.')
else:
    print(num,'is NOT a palindrome')