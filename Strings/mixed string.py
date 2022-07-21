#Create a mixed String using the following rules
'''Given two strings, s1 and s2. Write a program to create 
   a new string s3 made of the first char of s1, then the last char of s2,
   Next, the second char of s1 and second last char of s2, 
   and so on. Any leftover chars go at the end of the result.'''

s1=input("Enter first string") 
s2=input("Enter another string")  
n=len(s1) if len(s1)>len(s2) else len(s2)
s3=''
s2=s2[::-1]
for i in range(n):
    if i <len(s1):
        s3+=s1[i]
    if i< len(s2):
        s3+=s2[i]
print(s3)    
