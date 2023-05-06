'''
Given a nested list and update the list with sub list ["h", "i", "j"] in such a way that it will look like the following list.
'''

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
new = ["h", "i", "j"]
list1[2][1][2].extend(new)

print(list1)