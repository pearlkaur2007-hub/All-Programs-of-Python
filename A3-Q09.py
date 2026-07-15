#9. Write a recursive function to solve the Tower of Hanoi problem and print the moves.
def TOH(n,A,B,C):
    if n>0:
        TOH(n-1,A,C,B)
        print("Move disk from",A,"to",C)
        TOH(n-1,B,A,C)
n=int(input("Enter no of disks for Tower of Hanoi"))
TOH(n,1,2,3)