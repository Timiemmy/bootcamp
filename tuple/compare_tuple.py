'''
Implement a function which takes a string (sentence) as a parameter
and returns a tuple in which the words from the given sentenced are ordered based on their length.
'''

def order_words(p_text):
    words = p_text.split()
    nested_list = list()
    for word in words:
        nested_list.append((len(word), word))
    nested_list.sort()
    result = list()
    for length, word in nested_list:
        result.append(word)
    return tuple(result)

print(order_words("Python is my favorite programming language"))