'''
Implement a function which takes as a parameter a tuple and return a new tuple but only have even index elements from original tuple.
'''

def even_index_items(p_tuple):
    result_list = []
    for index, value in enumerate(p_tuple):
        if index % 2 == 0:
            result_list.append(value)
    result_tuple = tuple(result_list)
    return result_tuple


my_tuple = ("a", "b", "c", "d", "e", "f", "g")
print(even_index_items(my_tuple))
