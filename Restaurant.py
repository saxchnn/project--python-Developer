# Defining menu of the Restaurant
menu = { 'Pizza':250,'Pasta':140,'Burger':110,"Macroni":100,"Salad":120,'Water':20}
print(f"Welcome to Sachin's Restaurant")
print(f" Pizza:Rs 250 \n Pasta:Rs 140 \n Burger:Rs 110 \n Macroni:Rs 100 \n Salad:Rs 120 \n Water :Rs 20 \n")
order_total = 0
item_1 = input("Enter the Name of the item you want to order = ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order ")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item (Yes/No) = ")
if another_order =="Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order ")
    else:
        print(f"Ordered item {item_2} is not available ! ")
print(f"The Total amount of items to pay is {order_total}")