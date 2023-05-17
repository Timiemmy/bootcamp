'''
Implement a function which takes a dictionary as a parameter and returns new dictionary.
 In new dictionary the keys remain same but values will be another nested dictionary.
 Nested dictionary's keys will be values from original dictionary and values will be length of values from original dictionary.
(I know it is confusing, see example below you will understand it :) )
'''

names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}

def value_length(p_dict):
    new = {}
    for key, values in p_dict.items():
        new[key] = {}
        new[key][values] = len(values)

    return new

print(value_length(names_dict))