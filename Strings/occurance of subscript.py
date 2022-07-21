#Find all occurrences of a substring in a given string by ignoring the case
str1=input("Write something")
sub_str=input("Enter sub string to be checked:")
t=str1.lower()
count=t.count(sub_str.lower())
print(count)
