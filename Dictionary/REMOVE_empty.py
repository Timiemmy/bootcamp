'''
Implement a function which takes as a parameter dictionary and removes empty items from it and return new dictionary.
If there is not any empty item in the dictionary it will return itself.
'''

custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : 20
}

def remove_empty_items(n):
    new = {}
    for key, value in list(n.items()): # here i convert to list to avoid error.
        if value is None:
            n.pop(key)
        else:
            new[key] = value
    print(new)
remove_empty_items(custom_dict)