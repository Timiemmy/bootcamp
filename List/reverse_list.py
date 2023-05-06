custom_list = [1,2,3,4,5,6,7,8,9,10]
 #  string variable
reverse_list = []  # Empty String
count = len(custom_list) # Find length of a string and save in count variable
while count > 0:
    reverse_list.append(custom_list[count - 1 ]) # save the value of str[count-1] in reverseString
    count = count - 1 # decrement index
print("The reversed list using a while loop is: ",reverse_list)


print(custom_list[9::-1])
print(custom_list[len(custom_list)::-1])
print(custom_list[::-1])