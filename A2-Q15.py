#15. Write a Python program to count the occurrence of each word in a given sentence using a 
#dictionary.
sentence=input("Enter a sentence: ").lower()
senten=sentence.split()
d={}
for i in senten:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    print(key,':',value)