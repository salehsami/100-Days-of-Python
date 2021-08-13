# step 1
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Enter a guess word").lower()
for word in chosen_word:
    if word == guess:
        print(True)
    else:
        print(False)
