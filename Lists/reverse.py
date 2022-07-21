#reverse a list in python
l=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    a=input("Enter the element:")
    l.append(a)
print(l)    
l.reverse()
print(l)
