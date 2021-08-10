# Treasure Map
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
map[horizontal - 1][vertical - 1] = "X"
print(row1, "\n", row2, "\n", row3)






'''
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = position[0]
vertical = position[1]
if horizontal == 1:
    if vertical == 1:
        row1[0] = input("X")
    elif vertical == 2:
        row1[1] = input("X")
    elif vertical == 3:
        row1[2] = input("X")
    else:
        print("Enter correct data")
    
elif horizontal == 2:
    if vertical == 1:
        row2[0] = input("X")
    elif vertical == 2:
        row2[1] = input("X")
    elif vertical == 3:
        row2[2] = input("X")
    else:
        print("Enter correct data")
elif horizontal == 3:
    if vertical == 1:
        row3[0] = input("X")
    elif vertical == 2:
        row3[1] = input("X")
    elif vertical == 3:
        row3[2] = input("X")
    else:
        print("Enter correct data")
else:
    print("Enter correct data")'''
