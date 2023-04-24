height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

body_mass_index = round(weight / (height**2),2)

if body_mass_index < 18.5:
    print('You are underweight')
elif body_mass_index > 18.5 and body_mass_index < 25:
    print('your weight is normal')
elif body_mass_index > 25 and body_mass_index < 30:
    print('You are overweight')
elif body_mass_index>30 and body_mass_index < 35:
    print('You are Obese')