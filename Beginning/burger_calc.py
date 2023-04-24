Mini_Burger=5
Normal_Burger=8
Large_Burger=10

user = input('Which size do you want to buy? M, N, L ')
if user == 'M':
    Mushroom = input('Do you want to add Mushroom? Y or N ')
    Cheese = input('How about extra cheese? Y or N ').capitalize()
    if Mushroom == 'Y' and Cheese == 'Y':
        print(f'Total money is ${Mini_Burger+1+1}')
