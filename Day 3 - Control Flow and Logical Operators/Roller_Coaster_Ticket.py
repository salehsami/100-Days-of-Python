# Roller coaster Ticket
print("WWelcome to the RollerCoaster")
height = int(input("Enter your height in cm: "))
bill = 0
if height >= 120:
    print("You can ride  the Roller Coaster")
    age = int(input("What is your age: "))
    if age < 12:
        print("Your Ticket will be $5")
        bill += 5
    elif 12 <= age <= 18:
        print("Your Ticket will be $7")
        bill += 7
    else:
        print("Your Ticket will be $12")
        bill += 12

    photos = input("You want photos yes or no: ")
    if photos == "yes":
        print("photos ticket will be $3")
        bill += 3

    print(f"Your total Ticket is ${bill} ")

else:
    print("You can't ride the Roller Coaster")
