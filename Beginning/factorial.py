# Calculating factorial using math module
'''''
import math
fact = math.factorial

num = int(input('Enter any number: '))
ans = fact(num)

print(f'The factorial of {num} is {ans}')
'''

# Calculating factorial using recursion
'''''
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        n * fact(n - 1)


n =4 #int(input('Enter any number: '))
ans = fact(n)
print("Factorial of", n, "is", ans)
'''

# Calculating using if else
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)