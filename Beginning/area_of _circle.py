import math
pi = math.pi

user = int(input('Input the radius: '))

area = round(pi * (user**2), 2)

print(f'The area of circle is: {area}')