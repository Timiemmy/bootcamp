'''
Implement a function which takes as a parameter List and add elements to a Set and return a set.
'''

my_set=set()
def adding_set(nums):
    for num in nums:
        my_set.add(num)

    return my_set

my_list = [3,4,5,1,1,3,4,9,8]
print(adding_set(my_list))