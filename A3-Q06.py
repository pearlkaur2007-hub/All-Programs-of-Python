#6. Write a recursive function to convert a decimal number to binary.
def deci_to_bin(num):
    if num==0:
        return 0
    deci_to_bin(num//2)
    print(num%2, end='')
num1=int(input("Enter decimal number: "))
print("The binary equivalent is: ", end=" ")
deci_to_bin(num1)