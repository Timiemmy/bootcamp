'''
Use find and string slicing to extract the portion of the string
after the colon character and then use the float function to convert the extracted string into a floating point number.
'''

custom_string = 'X-MAPDS-Confidence:0.8475'
output = custom_string.find(':')
print(custom_string[output+1:])