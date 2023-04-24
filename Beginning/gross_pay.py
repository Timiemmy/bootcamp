''''
Instruction:
Rewrite the Gross Pay Project (Project 3) program to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
Here again the program prompts the user for hours and rate per hour to compute gross pay.
You need to take into account that the result has exactly two digits after the decimal place.

'''
Hours = float(input('Enter hours worked: '))
Rate = float(input('Enter rate per hour: '))


if Hours < 40:
    pay = Hours * Rate
else:
    overtime = Hours - 40
    pay = round(40 * Rate + overtime * Rate*1.5, 2)

print(f'Pay is {pay}')