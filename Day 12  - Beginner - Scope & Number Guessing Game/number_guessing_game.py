import random
title = """"
   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/

"""
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Type 'easy' or 'hard': ")
computer_guess = random.randint(1, 101)
def easy():
    attempts = 10
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == computer_guess:
            print(f"You got it!. The answer was {computer_guess}")
            break
        elif guess < computer_guess:
            print("Too low")
            print("Guess again")
        else:
            print("Too high")
            print("Guess again")
        attempts -= 1

def hard():
    attempts = 5
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == computer_guess:
            print(f"You got it!. The answer was {computer_guess}")
            break
        elif guess < computer_guess:
            print("Too low")
            print("Guess again")
        else:
            print("Too high")
            print("Guess again")
        attempts -= 1

def difficulty():
    if level == "easy":
        easy()
    elif level == "hard":
        hard()
    else:
        print("Enter correct data")

difficulty()
