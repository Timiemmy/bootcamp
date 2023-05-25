'''
There are three Sets are given. Write a program that finds the difference of them.
'''


a = {1, 2, 3, 40, 50, 300, 400}
b = {10, 20, 30, 40, 300}
c = {100, 200, 300, 400}

d = a.difference(b, c)

print(d)
print(a-b-c) # Another way