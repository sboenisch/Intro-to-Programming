import time
import random

#Grabbing objects
sword = 0
assists = 9

choices = ("You can only chose between A, B or C.")


#Delays the print function
def printSleep(text):
    print(text +"\n")
    time.sleep(2)


#Introduction of the adventure game
def start():
    printSleep("Today is your great game against Chicago Bulls with their")
    printSleep("superstar Michael Jordan. Your long term rival.")
    printSleep("You prepared weeks for this insane game.")
    printSleep("The game is about to end. The current scores are 88:88.")
    printSleep("10 seconds are left.")
    printSleep("You have the ball. What will you do?")
    #Choices
    printSleep("A. Pass the ball to your teammate.")
    printSleep("B. Triple the ball towards 3-point line.")
    printSleep("C. Stand still.")
    answer = input(">>> ").lower()
    if "a" in answer:
        teammate()
    elif "b" in answer:
        threePointLine()
    elif "c" in answer:
        scottiePippen()
    else:
        printSleep(choices)
        intro()


#Option throwing a rock to the orc
def teammate():
    # printSleep("The orc is stunned, but regains control. He begins ")
    # printSleep("running towards you again. Will you:")
    # printSleep("A. Run\nB. Throw another rock\nC. Run towards a nearby cave\n")
    # answer = input(">>> ").lower()
    # if "a" in answer:
    #     option_run()
    # elif "b" in answer:
    #     printSleep("You decided to throw another rock, as if the first")
    #     printSleep("rock thrown did much damage. The rock flew well over the ")
    #     printSleep("orcs head. You missed. \n\nYou died!")
    # elif "c" in answer:
    #     option_cave()
    # else:
    #     print(choices)
    #     option_rock()


def threePointLine():
    printSleep("You stand in front of the three point line. You have ")
    printSleep("several options. ")
    # answer = input(">>> ").lower()
    # if "y" in answer:
    #     sword = 1
    # else:
    #     sword = 0
    while True:
        printSleep("What do you do next?")
        printSleep("A. Cross over\nB. Throw 3 point\nC. Run towards basket")
        answer = input(">>> ").lower()
        if "a" in answer:
            printSleep("Really? You're going to hide in the dark? I think ")
            printSleep("orcs can see very well in the dark, right? Not sure, but ")
            printSleep("I'm going with YES, so...\n\nYou died!")
            break()
        elif "b" in answer:
            printSleep("You laid in wait. The shimmering sword attracted ")
            printSleep("the orc, which thought you were no match. As he walked ")
            printSleep("closer and closer, your heart beat rapidly. As the orc ")
            printSleep("reached out to grab the sword, you pierced the blade into ")
            printSleep("its chest. \n\nYou survived!")
            break()
        elif "c" in answer:
            printSleep("As the orc enters the dark cave, you sliently ")
            printSleep("sneak out. You're several feet away, but the orc turns ")
            printSleep("around and sees you running.")
            option_run()
            break()



def scottiePippen():
    printSleep("Suddenly Scottie Pippen hit the ball. You lost the ball. ")
    printSleep("You will:")
    printSleep("A. Do nothing.\nB. Foul Pippen\nC. Try to steal the ball.")
    answer = input(">>> ").lower()
    if "a" in answer:
        printSleep("Pippen scores. Chicago Bulls won 90:88. You lost.")
    elif "b" in answer:
        printSleep("You fouled Pippen but too late. Pippen scores")
        printSleep("and scored the free throw, too. You lost.")
    elif "c" in answer:
        stealBall()
    else:
        printSleep(choices)
        scottiePippen()

def stealBall():
    printSleep("You stole the ball from Scottie Pippen. The clock is running.")
    printSleep("7...6...5...You pass the ball to your teammate.")
    printSleep("Will you run towards the basket [Y/N]?")
    answer = input(">>> ").lower()
    if "y" in answer:
        assit += 1
        print("Your teammates throw and hits!!!! Miami Heat wins 91:88")
    elif:
        printSleep("You did nothing. Your teammates misses the throw. ")
        printSleep("Game ends. It is a tie 88:88")
    else:
        printSleep("Please choose.")
        stealBall()


start()
