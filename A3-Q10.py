#10. Write a recursive function to generate all subsets of a set (power set).
s=[]
n=int(input("Enter no. of elements:"))
for i in range(n):
    i=int(input("Enter element:"))
    s.append(i)
s=set(s)
s=list(s)
def power_set(s, index=0, current=[]):
    if index == len(s):
        print(current)
        return
    power_set(s, index + 1, current + [s[index]])
    power_set(s, index + 1, current)
power_set(s)
