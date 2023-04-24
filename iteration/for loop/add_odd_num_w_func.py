
'''
Implement a function that calculates the sum of all odd numbers from 1 to 100 by using range() function inside loop.

'''

'''''
def add_odd_numbers(number):
    odd_number = 0
    for odd in range(number):
        if odd % 2 != 0:
            odd_number += odd
    return odd_number


result = add_odd_numbers(100)
print(result)
'''

# Sum up of even number
def add_odd_numbers(start, stop):
    even_number = 0
    for odd in range(start, stop):
        if odd % 2 == 0:
            even_number += odd
    return even_number


result = add_odd_numbers(1, 101)
print(result)