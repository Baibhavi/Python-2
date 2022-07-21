#Create a string made up of 1st , middle and last character of the given string
s=input("Write Something: ")
n=len(s)
print(s)
if n%2!=0:
    new_word=s[0]+s[(n-1)//2]+s[n-1]
else:
    new_word=s[0]+s[(n-2)//2]+s[n//2]+s[n-1]
print(new_word)    
