'''
Find the value of 50 in a given list, and if it is present, replace  the first occurrence of a value with 5.
'''

list1 = [10, 10, 5, 15, 50, 50, 20]

if 50 in list1:
    num = list1.index(50)
    list1[num] = 5

print(list1)