#Electricity bill
n=int(input("Enter the units of electricity consumed:"))
sum=0
if n<=100:
    sum=0
elif n<=200:
    sum+=(100*0)+ (n-100)*5
else:
    sum+= (100*0)+ (100*5) + (n-200)*10
print("Your Electricity bill = ",sum)  
