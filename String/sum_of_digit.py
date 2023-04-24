'''
Create a function that takes two digit number from console and returns sum of digits.
e.g. if the input was 45, then the output should be 4 + 5 = 9


def sum_of_two_digits():
    user = input('Input two digit: ')
    answer = int(user[0]) + int(user[-1])
    return answer



print(sum_of_two_digits())
'''

# For 3 digit


def sum_of_digits():
    user = input('Input two digit: ')
    add = 0
    for i in user:
        add += int(i)
    return add

print(sum_of_digits())