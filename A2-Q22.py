#22. Write a Python program to find the longest substring in a string without repeating 
#characters.
string=str(input("Enter a string: "))
max_sub=''
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        sub = string[i:j]
        if len(set(sub)) == len(sub):
            if len(sub) > len(max_sub):
                max_sub = sub
print("Max substring:", max_sub)