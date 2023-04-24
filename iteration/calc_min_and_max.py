'''
Write another program that prompts for a list of numbers as we did in previous exercises
and at the end prints out both the maximum and minimum of the inputted numbers.
'''


def min_and_max(num):
    try:
        val = float(num) # Convert to float
        return val
    except (ValueError, TypeError): # prints out if error
        print('Error, please enter numeric input')
        return False


count = []
total = 0.0
average = 0.0
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    else:
        count.append(user_input)
    number = min_and_max(user_input)
    if not number:
        continue


if count != '':
    print(f'You entered {count}. \nThe maximum is {max(count)}, and the minimum is {min(count)}')
else:
    print('You have to input at least 3 numbers to get result')
