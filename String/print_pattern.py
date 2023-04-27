'''
Create a function which takes as parameter integer number (n) and based on this number it prints the following start pattern using nested loop and string formatting.
So if n equals 5 the maximum number of stars (*) will be 5 in the pattern.
'''

def print_pattern(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('*', end=' ')
        print()
# To print out the second step
    for i in range(n, 0, -1): # I put n at first, so it starts from the back
        for j in range(0, i-1):
            print('*', end=' ')
        print()



print_pattern(10)