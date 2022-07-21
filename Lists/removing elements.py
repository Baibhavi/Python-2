'''Remove empty strings from list
lst=['State',' ','City','Town',' ','Country']'''
lst=['State',' ','City','Town',' ','Country']
lst2=[]
for i in lst:
    if i == ' ':
        lst.remove(i)
print(lst)        
#another way
lst2=list(filter(None,lst))
print(lst2)
