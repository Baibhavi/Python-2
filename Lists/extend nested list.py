'''Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub list to add:
sub_list = ["h", "i", "j"]'''
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
print(list1)
list1[2][1][2].extend(sub_list)
print(list1)
