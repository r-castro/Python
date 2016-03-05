import random


def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    worksum = die1 + die2
    print("Player rolled %d + %d = %d" % (die1, die2, worksum))

    return worksum

sum = roll_dice()

if sum == 7 or sum == 11:
    gamestatus = "WON"
elif sum == 2 or sum == 3 or sum == 12:
    gamestatus = "LOST"
else:
    gamestatus = "CONTINUE"
    myPoint = sum
    print("Point is", myPoint)

while gamestatus == "CONTINUE":
    sum = roll_dice()

    if sum == myPoint:
        gamestatus = "WON"
    elif sum == 7:
        gamestatus = "LOST"

if gamestatus == "WON":
    print("Player wins")
else:
    print("Player loses")
