#2. Write a recursive function to find the GCD of two numbers using the Euclidean algorithm.
def gcd(n1,n2):
    if n2==0:
        return n1
    return gcd(n2, n1%n2)
n1=int(input('Enter number: '))
n2=int(input('Enter number: '))
print('The GCD of ',n1,'& ', n2, 'is ', gcd(n1,n2))