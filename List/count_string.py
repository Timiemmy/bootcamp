'''
Implement a function which takes the string type list as a parameter and returns the count of the number of strings
where the string length is 2 or more and the first and the last characters are same.
'''

def count_words(p_list):
    list = []
    for i in p_list:
        if len(i) >= 2:
            if i[0] == i[-1]:
                total = list.append(i)
    print(len(list))


list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
count_words(list1)