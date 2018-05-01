import random

print("WELCOME TO THE GUESSING GAME OF THE YEAR.")
print("What is your name buddy?", end=" ")
name = input()
print("Well!!", name, "You have 5 times to find the right number")

guessTaken = 0
number = random.randint(1,30)

for guessTaken in range(5):
    print("Take a guess", name)
    guess = input(">>> ")
    guess = int(guess)

    if guess == number:
        break
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")

if guess == number:
    guessTaken = str(guessTaken + 1)
    print("Holy shit, you made it after", guessTaken, "guesses.")
if guess != number:
    number = str(number)
    print("Oh dam bro you gonna retry mannnn")

print("you have another chance to retry")



