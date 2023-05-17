import pprint
''''
custom_list = [1, 2, 3, 4, 5]
custom = str(custom_list)
string = custom.split()

new = '|'.join(string)

print(str(new))
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2].insert(1, 7000)
for i in list1:
    print(i)