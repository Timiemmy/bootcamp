'''
Create a program which prints out student names and their score as shown below

names and scores lists are given
names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]
'''
'''
names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]

for index in range(len(names)):
    print(f'{names[index]} {scores[index]}')
'''
# To make it align
names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]
print('{0:<10} {1:<5}'.format('names', 'score'))# here we give 10 and 5  left alignment respectively.
for index in range(len(names)):
    name = names[index]
    score = scores[index]
    print('{0:<10} {1:<5}'.format(name, score))# here also, we give 10 and 5 left alignment respectively.