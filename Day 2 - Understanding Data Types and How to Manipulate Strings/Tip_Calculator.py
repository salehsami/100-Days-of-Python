print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
bill = int(bill)
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip = int(tip)
tip = tip/100
total =tip * bill
final_bill = total + bill
split = input("How many people to split the bill? ")
split = int(split)
pay = final_bill/split
pay = round(pay, 2)
print(f"Each person should pay: ${pay}")

# Changings
'''
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip = tip/100
total = tip * bill
final_bill = total + bill
split = int(input("How many people to split the bill? "))
pay = final_bill/split
pay = "{:.2f}".format(pay)
print(f"Each person should pay: ${pay}")
'''
