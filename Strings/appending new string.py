#Append a new string in the middle of the given string
s=input("Enter a string")
s2=input("Enter a new string")
if len(s)%2==0:
    new_string=s[0:len(s)//2:]+s2+s[len(s)//2:len(s)]
print(new_string) 
