# entering the goal in maze
def turnright():
    turnleft()
    turnleft()
    turnleft()
while front_is_clear():
    move()
while not at_goal():
    if right_is_clear():
        turnright()
        move()
    elif front_is_clear():
        move()
    else:
        turnleft()
        move()
