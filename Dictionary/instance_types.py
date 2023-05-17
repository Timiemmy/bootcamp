'''
Implement a function which takes a List a parameter and groups them according to their data types (integer or string) and return dictionary.
'''

custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]

def group_types(n):
    new = {}
    for i in n:
        if isinstance(i, int):
            new[i] = 'integer'

        else:
            new[i] = 'String'

    return new

print(group_types(custom_list))

def group_types(n):
    new = {}
    for i in n:
        if type(i) == int:
            new[i] = 'integer'

        else:
            new[i] = 'String'

    return new

print(group_types(custom_list))