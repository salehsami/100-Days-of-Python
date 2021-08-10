# paying bill
import random
names_string = input("Give everybody's names, separated by a comma. ")
names = names_string.split(", ")
amount = len(names)
random_no = random.randint(0, amount - 1)
lucky_one = names[random_no]
print(lucky_one + " is going to buy the meal today")
