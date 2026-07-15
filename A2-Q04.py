#4. Write a Python program to iterate through a string and count the number of vowels present
#in it.
s1=input('Enter a string: ')
n=len(s1)
c=0
for ele in s1:
    if(ele=='a'or ele=='e' or ele=='i'or ele=='o'or ele=='u'):
        c+=1
print('The number of vowels in the srting: ',c)