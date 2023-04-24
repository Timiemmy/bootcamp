'''
Implement a function that takes an integer number as a parameter and returns factorial of this number.
'''

num = int(input('Enter Any Number: '))


def factorial(p_num):
    fact = 1
    if p_num < 0:
        return 'Factorial does not exist for negative numbers'
    elif p_num == 0:
        return f'The factorial of {num} is 1'
    else:
        for i in range(1, p_num+1):
            fact = fact * i
        return f'The factorial of {p_num} is {fact}'

print(factorial(num))