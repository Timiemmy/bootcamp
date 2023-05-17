'''
Implement a function which takes dictionary as a parameter and returns multiplication of values of this dictionary.
'''

my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
def multiply_values(n):
    result = 1
    for value in n.values():
        result *= value
    return result

print(multiply_values(my_dict))