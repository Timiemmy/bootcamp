'''
Given two lists create a third list by picking an odd-index element from the first list and even-index elements from the second.
'''

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
list_three = []

for num in list_one:
    if list_one.index(num) % 2 != 0:
        list_three.append(num)

for num in list_two:
    if list_two.index(num) % 2 == 0:
        list_three.append(num)

print(list_three)


# Using list methods
third_list = list()
odd_elements = list_one[1::2]
even_elements = list_two[0::2]
third_list.extend(odd_elements)
third_list.extend(even_elements)
print(third_list)