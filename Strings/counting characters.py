# Count all letters, digits, and special symbols from a given string
n=input("Write something:")
letters=digits=sp=0
for i in range(len(n)):
    if n[i].isalpha():
        letters+=1
    elif n[i].isdigit():
        digits+=1
    else:
        sp+=1    
print("Letters=",letters)
print("digits=",digits)
print("Special Symbol=",sp)
