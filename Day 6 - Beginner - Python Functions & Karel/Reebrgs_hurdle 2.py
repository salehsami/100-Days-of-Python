# while loop practice
def turnright():
    turnleft()
    turnleft()
    turnleft()
def jump():
    move()
    turnleft()
    move()
    turnright()
    move()
    turnright()
    move()
    turnleft()
while not at_end():
    if hurdle:
        jump()
    else:
        move()
