'''
Implement a function which takes a parameter N and returns Set of numbers which are divisible by 3 and 4 between 0 and N.
'''

def divisible_by_3and4(n):
    the_num = set()
    for num in range(n):
        if num % 3 == 0 and num % 4 == 0:
            the_num.add(num)

    return the_num

print(divisible_by_3and4(100))