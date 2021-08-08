# Treasure island game
print("Welcome to treasure island")
print("Your mission is to find the treasure ")
cross = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"").lower()
if cross == "left":
    swim = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()
    if swim == "wait":
        door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, One yellow and one blue. Which colour do you choose? ").lower()
        if door == "yellow":
            print("You win")
        elif door == "red":
            print("It's a room of fire. Game Over")
        elif door == "blue":
            print("It's a room full of beasts. Game Over")
        else:
            print("Game Over")

    else:
        print("Game Over")
else:
    print("Game Over")


