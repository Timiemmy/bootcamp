print('Welcome to trip cost calculator')
day = input('How many days stay: ')
hotel_cost = input('How much hotel cost per night: ')
flight = input('How much is flight: ')
rental = input('Enter price if you need any rental: ')
others = input('Enter other possible expenses: ')

hotel_spent = int(day) * float(hotel_cost)
rental_spent = int(day) * float(rental)
total = round(hotel_spent + rental_spent + int(flight), 2)

print(f'Total cost: {total}')