# Love calculator
print("Welcome to the love calculator! ")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
both = name1 + name2
both = both.lower()
t = both.count("t")
r = both.count("r")
u = both.count("u")
e = both.count("e")
F = both.count("l")
A = both.count("o")
L = both.count("v")
S = both.count("e")
true_both = t + r + u + e
false_both = F + A + L + S
love_score = str(true_both) + str(false_both)
love_score = int(love_score)
if 90 < love_score < 10:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score > 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
