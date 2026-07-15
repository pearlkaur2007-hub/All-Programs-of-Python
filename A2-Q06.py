#6. Write a Python program to create a list of squares of numbers from 1 to 10 using list 
#comprehension.
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)
new_l1=[l1[i]*l1[i] for i in range(len(l1))]
print(new_l1)