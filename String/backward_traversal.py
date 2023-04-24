'''
Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
'''
'''''
# Using while loop
user = input('Enter a string: ')
index = 0
while len(user) > index:
    letter = user[]
    print(letter[::-1])
    index -= 1
'''
# Using while loop
str = input('Enter a string: ') #  string variable
reverse_String = ""  # Empty String
count = len(str) # Find length of a string and save in count variable
while count > 0:
    reverse_String += str[ count - 1 ] # save the value of str[count-1] in reverseString
    count = count - 1 # decrement index
print("The reversed string using a while loop is : ",reverse_String)
'''
user = input('Enter a string: ')
for char in user:
    print(char[1])
'''