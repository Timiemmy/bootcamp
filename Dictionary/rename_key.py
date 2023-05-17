'''
Write a program which renames the key in the dictionary, you need to rename key city to address in the following dictionary.
'''

my_dict = {
    "name": "Edy",
    "age":30,
    "salary": 5000,
    "city": "London"
}

my_dict["address"] = my_dict["city"]
del my_dict["city"] # It has to be removed, or else it adds it back
print(my_dict)