#19. Write a Python program to create a custom iterator that generates numbers from 1 to N.
class gen:
    def __init__(self,n):
        self.a=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.a>self.n:
            raise StopIteration
        val=self.a
        self.a+=1
        return val
n=int(input("Enter n:"))
for num in gen(n):
    print(num)