# Your life in weeks challenge

age = input("What is your current age: ")
left = 90 - int(age)
day = 365 * left
day = round(day, 5)
week = 52 * left
week = round(week, 4)
month = 12 * left
month = round(month, 3)
print(f"You have {day} days, {week} weeks and {month} months left")
