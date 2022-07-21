#Create a new string made of first , middle and last character of the given strings:
'''given: s1="America"
          s2="Japan"
   output: AJrpan       '''
s1=input("Enter the first string:")
s2=input("Enter another string:")
if len(s1)%2!=0 and len(s2)%2!=0:
    new_string=s1[0]+s2[0]+s1[(len(s1)-1)//2]+s2[(len(s2)-1)//2]+s1[len(s1)-1]+s2[len(s2)-1]
print(new_string) 
