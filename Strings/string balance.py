# String characters balance Test
'''Write a program to check if two strings are balanced.
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character's position doesn't matter.'''
s1=input("Enter first string") 
s2=input("Enter another string") 
result=True
for i in range(len(s1)):
    if s1[i] in s2:
        continue
    else:
        result=False
print(result)
