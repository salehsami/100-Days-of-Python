import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"Pssst, the solution is {chosen_word}.")
end_of_game = False
display = []
for i in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter {guess}')
        if letter == guess:
            display[position] = letter
print(display)
if "_" not in display:
    print("You win")
