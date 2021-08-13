import random
import Hangman_asscii
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False
print(f"Pssst, the solution is {chosen_word}.")
display = []
for i in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guessed this letter")
    for position in range(word_length):
        letter = chosen_word[position]
#        print(f"Current position: {position}\n Current letter  {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print("You lost a life")
        lives = -1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(Hangman_asscii.HANGMAN(lives))
