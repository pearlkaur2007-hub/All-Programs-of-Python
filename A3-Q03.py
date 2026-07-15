#3. Write a recursive function to count the number of digits in a number.
def cnt(n):
    if n==0:
        return 0
    return 1 + cnt(n // 10)
n = int(input('Enter the number: '))
if n == 0:
    print("The number of digits is: 1")
else:
    print("The number of digits is: ", cnt(n))