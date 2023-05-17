'''
Implement a function which takes a tuple as a parameter and returns another tuple with two elements.
First element is the most frequent item and the second element of number of repetition.
'''

def most_frequent(p_tuple):
    first_element = p_tuple[0]
    value = 0
    for i in p_tuple:
        count = p_tuple.count(i)
        if count > value:
            value = count
            first_element = i
    return first_element, value



my_tuple = ("a", "b", "c", "d", "e", "a", "c", "e", "b", "e", "c", "a", "f", "e", "r")
print(most_frequent(my_tuple))
