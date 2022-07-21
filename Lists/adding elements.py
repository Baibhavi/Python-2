#Add the following item after a specified item (i.e,  add 7000 after 6000)
list=[1000,2000,3000,4000,5000,6000,8000,9000]
print(list)
n=int(input("Enter the number after which you want to add: "))
i=list.index(n) 
i=i+1
a=int(input("Enter the number to be added: "))
list.insert(i,a)
print(list)
#for nested list
list2=[1000,[2000,3000,4000,[5000,6000],8000],9000]
list2[1][3].append(7000)
print(list2)
