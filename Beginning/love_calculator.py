'''
Write a program to test the compatibility between two people.

Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 85, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 70, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
'''
print('Welcome to the love calculator')
first_name = str(input('Input your name: '.lower()))
lover_name = str(input('Input lover\'s name: '.lower()))

both_name = first_name + lover_name

t = both_name.count('t')
r = both_name.count('r')
u = both_name.count('u')
e = both_name.count('e')
true = t+r+u+e

l = both_name.count('l')
o = both_name.count('o')
v = both_name.count('v')
e = both_name.count('e')
love = l+o+v+e

true_love = int(str(true)+ str(love))

if true_love < 10 or true_love > 85:
    print(f"Your score is {true_love}, you go together like coke and mentos.")

elif 40 < true_love < 70:
    print(f"Your score is {true_love}, you are alright together.")

else:
    print(f"Your score is {true_love}.")