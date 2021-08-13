# step 1
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Pssst, the solution is {chosen_word}.")
display = []
count = 0
for word in chosen_word:
    display.append("_")
print(display)
guess = input("Guess a letter").lower()
for letter in chosen_word:
    count = count + 1
    if letter == guess:
        display[count - 1] = letter
print(display)
