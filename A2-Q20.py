#20. Write a Python program to implement a generator function to generate Fibonacci numbers 
#up to N.
def fibo(n,a=0,b=1):
    if n==0:
        return
    yield a
    yield from fibo(n-1,b,a+b)
n=int(input("Enter no of elements for fibonacci series: "))
for num in fibo(n):
    print(num)