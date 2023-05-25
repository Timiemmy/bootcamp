'''
Implement a function which takes list of sets as a parameter and returns one set which includes all elements from the given list of sets.
'''


def convert_ls(list_of_sets):
    new_set = list_of_sets[0] | list_of_sets[1] | list_of_sets[2] | list_of_sets[3] | list_of_sets[4]
    return new_set


def convert_ls(p_ls):
    final_set = set()
    for item in p_ls:
        final_set = final_set.union(item)
    return final_set

# Another way

list_of_sets = [
    {10,20,30,40,50},
    {"apple", "orange","limon","pear"},
    {"London", "Berlin", "Paris"},
    {"Python", "Java", "Swift"},
    {10, "ten", "20", 20}
]

print(
    convert_ls(list_of_sets)
)

print(len(list_of_sets))