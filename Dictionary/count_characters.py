'''
Implement a function that takes a String as a parameter and returns a dictionary with characters as keys from the String
and values are the occurrence of characters in the String.
Basically we are counting the occurrence of characters in a given string and returning it as output in Dictionary.
'''

def count_characters(n):
    my_dict = {}
    for i in n:
        count = n.count(i)
        my_dict[i] = count
    return my_dict

print(count_characters("BABACDAS"))