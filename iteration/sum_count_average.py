'''
Write a program which repeatedly reads numbers until the user enters "done".
Once “done” is entered, print out the total, count, and average of the numbers.

If the user enters anything other than a number,
detect their mistake using try and except and print an error message and skip to the next number.
'''
'''
Step 1 - Create a function which checks for numbers using try and except block.

Step 2 - Inside while loop ask for input

Step 3 - Calculate count, sum and average'''

print("Calculate average of numbers. Type 'done' when you've entered all")
def sum_count_average(num):
    try:
        val = float(num) # Convert to float
        return val
    except (ValueError, TypeError): # prints out if error
        print('Error, please enter numeric input')
        return False


count = 0
total = 0.0
average = 0.0
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    number = sum_count_average(user_input)
    if not number:
        continue

    count += 1
    total = total + number


if count != 0:
    average = total/count
    print(average)
else:
    print('You have to input at least 2 numbers to get result')
