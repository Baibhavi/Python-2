#Create a string made up of all middle three characters of the given string
s=input("Write Something: ")
n=len(s)
if n%2!=0:
    new_string=s[(n-3)//2]+s[(n-1)//2]+s[(n+1)//2]
else:
    print("There's not three middle words")
print(new_string)    
