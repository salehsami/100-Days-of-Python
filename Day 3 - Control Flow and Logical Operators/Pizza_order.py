# Pizza order
print("Welcome to Python Pizza Deliveries")
price = 0
size = input("Which size pizza do you want? S, M or L:  ")
if size == "S" or "s":
    price += 15
elif size == "M" or "m":
    price += 20
elif size == "L" or "l":
    price += 25
else:
    print("Wrong data entered")

add_pepperoni = input("Do you want to pepperoni? Y or N: ")
if add_pepperoni == "Y" or "y":
    if size == "S" or "s":
        price += 2
    else:
        price += 3

extra_cheese = input("Do you want extra cheese? Y or N:  ")
if extra_cheese == "Y" or "y":
    price += 1
print(f"Your final bill is: ${price}.")
