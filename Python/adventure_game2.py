import time
import random

# Random game stats for the player
# points = random.randint(2, 50)
# assists = random.randint(0, 15)
# steals = random.randint(0, 10)

# Warning for invalid enters
choices = ("You can only choose between A, B or C.")


# Delays the print function
def printSleep(text):
    print(text + "\n")
    time.sleep(1)


def stats():
    print("Points: " + str(points))
    print("\nAssists: " + str(assists))
    print("\nSteals: " + str(steals))
    replay()


# Introduction of the adventure game Miami Heat vs. Chicago Bulls
def start():
    global points, assists, steals
    points = random.randint(2, 50)
    assists = random.randint(0, 15)
    steals = random.randint(0, 10)
    printSleep("Today is your great game against Chicago Bulls with their")
    printSleep("superstar Michael Jordan. Your long term rival.")
    printSleep("You prepared weeks for this insane game.")
    printSleep("The game is about to end. The current scores are 88:88.")
    printSleep("10 seconds are left.")
    printSleep("You have the ball. What will you do?")
    printSleep("A. Pass the ball to your teammate.")  # Choices
    printSleep("B. Triple the ball towards 3-point line.")
    printSleep("C. Stand still.")
    answer = input(">>> ").lower()
    if answer == "a":
        teammate()
    elif answer == "b":
        threePointLine()
    elif answer == "c":
        scottiePippen()
    else:
        printSleep(choices)
        start()


# Option throwing a rock to the orc
def teammate():
    printSleep("You pass the ball to your teammate Dwayne Wade.")
    printSleep("He is about to do his signature move aka the Flash.")
    printSleep("What will you do?")
    printSleep("""A: Nothing\nB: Going to the basket \n C: Set a block
    for your teammate.""")
    answer = input(">>> ").lower()
    if answer == "a":
        printSleep("""Dwayne Wade looses the ball and the Chicago Bulls
        scores to the win.""")
        printSleep("Chicago wins the game by 90:88.")
        stats()
    elif answer == "b":
        printSleep("Your teammate shoots! But he misses the basket.")
        printSleep("""The ball is still in the air. Thankfully your position
        is good.""")
        printSleep("""You rebound the ball and put it in!!! Miami Heat wins
        90:88""")
        stats()
    elif answer == "c":
        printSleep("""By setting up the block your teammate had the chance to
        go to the basket.""")
        printSleep("He scores!!! Miami Heat wins 90:88.")
        stats()
    else:
        print(choices)
        teammate()


def threePointLine():
    printSleep("You stand in front of the three point line. You have ")
    printSleep("several options. ")
    while True:
        printSleep("What do you do next?")
        printSleep("A. Cross over\nB. Throw 3 point\nC. Run towards basket")
        answer = input(">>> ").lower()
        if answer == "a":
            printSleep("""You cross the ball over but Michael Jordan steals you
            the ball.""")
            printSleep("""2 seconds later M.J. scores and lead the Chicago
            Bulls to the win.""")
            stats()
            break
        elif answer == "b":
            printSleep("""Only 3 seconds left. You jump into the air and shoot
            the ball.""")
            printSleep("""The ball touches the ring and bounce against the
            basket wall.""")
            printSleep("""A moment of silence. But suddenly the ball falls
            into the basket.""")
            printSleep("Miami Heat wins 91:88.")
            stats()
            break
        elif answer == "c":
            printSleep("""You pass the first enemy player. Then the second
            enemy player.""")
            printSleep("""""You lift off for the points but suddenly a huge
            figure is""")
            printSleep("in front of you and blocks you away.")
            printSleep("""A quick pass and Chicago Bulls scores and wins
            the game!""""")
            stats()
            break


def scottiePippen():
    printSleep("Suddenly Scottie Pippen hit the ball. You lost the ball. ")
    printSleep("You will:")
    printSleep("A. Do nothing.\nB. Foul Pippen\nC. Try to steal the ball.")
    answer = input(">>> ").lower()
    if answer == "a":
        printSleep("Pippen scores. Chicago Bulls won 90:88. You lost.")
        stats()
    elif answer == "b":
        printSleep("You fouled Pippen but too late. Pippen scores")
        printSleep("and scored the free throw, too. You lost.")
        stats()
    elif answer == "c":
        stealBall()
    else:
        printSleep(choices)
        scottiePippen()


def stealBall():
    printSleep("You stole the ball from Scottie Pippen. The clock is running.")
    printSleep("7...6...5...You pass the ball to your teammate.")
    printSleep("Will you run towards the basket [Y/N]?")
    answer = input(">>> ").lower()
    if answer == "y":
        print("Your teammates throw and hits!!!! Miami Heat wins 91:88")
        stats()
    elif answer == "n":
        printSleep("You did nothing. Your teammates misses the throw. ")
        printSleep("Game ends. It is a tie 88:88")
        stats()
    else:
        printSleep("Please choose.")
        stealBall()


def replay():
    gamechoice = input("You wanna play again [Y/N]?").lower()
    while True:
        if gamechoice == "y":
            start()
            break
        elif gamechoice == "n":
            printSleep("Thank you for playing the game!")
            break


start()
