'''
Set of items and set of restricted items are given, based on the beach type (family or normal)
the list of items should be printed to the console.
Restricted items are not allowed to family beach and everything else can be taken to normal beach except drugs.
'''

general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}

restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
}


user = input('Select Beach Type (1 - Family beach, 2 - Normal Beach): ')
if user == "1":
    for items in restricted_items:
        general_items.discard(items)

else:
    general_items.discard("Drugs")
print('See below the list of items that you can take.')
for item in general_items:
    print(f' \t {item}')