'''
Implement a function which takes integer number (n) as a parameter and returns dictionary with keys
from 1 to n and values are square of the numbers from 1 to n.
'''



def generate_dictionary(n):
    dict = {}
    for num in range(1, n+1):
        dict[num] = num**2
    return dict

print(generate_dictionary(5))
