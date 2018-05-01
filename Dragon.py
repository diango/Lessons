# Let's import random and time module
import random
import time

# Make a intro to the Dragon Game
def displayIntro():
    print("What is your name bro?", end=" ")
    name = input().upper()
    print("""{} is in aland full of dragons. In front of you,
        you see two caves. In one cave the Dragon in friendly
        and will share his treasure with you. The other dragon is 
        greedy and hungry, and will eat you on sight.""".format(name))


def chooseCave():
    cave = " "
    if cave != "1" or cave != "2":
        print("Choose one cave between 1 or 2")
        cave = input()
    
    return cave

def checkCave(chosenCave):
    print("You approch the cave........")
    time.sleep(2)
    print("and it's dark and spooky.....")
    time.sleep(2)
    print("A large dragon jump out in front of you! He opens his jaws and......")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print("He gives you his treasure!!!!!")
    else:
        print("Gobbles, you down in one bite!!!!")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Do you wanna play again.")
    playAgain = input()


