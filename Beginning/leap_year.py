'''
Write a program that works out whether if a given year is a leap year.
A normal year has 365 days, leap years have 366, with an extra day in February.

Three criteria must be taken into account to identify leap years:

This is how you work out whether if a particular year is a leap year.

The year must be evenly divisible by 4; If the year can also be evenly divided by 100, it is not a leap year;
**unless** the year is also evenly divisible by 400
'''

year = int(input('Input any year to know if it is leap year: '))
''''
if year % 4 == 0:
    if year % 100 == 0:
        if year%400 == 0:
            print(f'Year {year} is a leap year')
        else:
            print(f'Year {year} is not a leap year')
    else:
        print(f'Year {year} is a leap year')

else:
    print(f'Year {year} is a leap year')
'''