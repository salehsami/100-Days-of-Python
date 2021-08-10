# rock paper scissors
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
pc_choice = random.randint(0, 3)
print(f"Computer choose {pc_choice}")
if user_choice == 0 and pc_choice == 2:
    print("You win")
elif pc_choice > user_choice:
    print("You lose")
elif user_choice == pc_choice:
    print("It's a draw")
else:
    print("computer has not chosen the data correctly")
