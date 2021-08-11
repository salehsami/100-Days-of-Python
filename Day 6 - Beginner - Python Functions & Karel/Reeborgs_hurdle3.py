def turnright():
    turnleft()
    turnleft()
    turnleft()

def jump():
    turnleft()

    while wall_on_right():
        move()

    turnright()
    move()
    turnright()

    while front_is_clear():
        move()

    turnleft()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
