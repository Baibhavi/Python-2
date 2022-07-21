#Remove empty strings from a list of strings
str1=['his','her','','name','for','not','','broke']
for i in str1:
    if i=='':
        str1.remove(i)
print(str1)       
