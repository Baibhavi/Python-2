# Arrange the characters of strings in such a way that lowercase letters comes in first
'''given: NaTiVe
output:   aieNTV'''
n=input("Enter a string:")
lower=[]
upper=[]
for i in n:
    if i .islower():
        lower.append(i)
    else:
        upper.append(i)
sorted_string=''.join(lower+upper)
print(sorted_string) 
