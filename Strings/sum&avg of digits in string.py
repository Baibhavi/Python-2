#Calculate the sum and average of the digits present in a string
str=input("Enter string:")
s=0
div=0
for i in str:
    if i.isdigit():
        s+=int(i)
        div+=1
avg=(s/div)
print(avg)
