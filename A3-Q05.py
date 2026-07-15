#5. Write a recursive function to count occurrences of a character in a string.
def cnt(n,char,string,i):
    if i==n:
        print("No occurrences found.")
        return 0
    if string[i]==char:
        return 1+cnt(n,char,string,i+1)
    else:
        return cnt(n,char,string,i+1)
    
string=str(input("Enter the string: "))
char=str(input("Enter an alphabet: "))
i=0
n=len(string)
print("The occurrences of a character",char,"in a string",cnt(n,char,string,0))
