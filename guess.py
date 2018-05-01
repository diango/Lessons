import random

# Let's initilize the Game
print("******** Welcome to GUESSING GAMESSS ***********")

# Ask the player a name
print("What is your name buddy?", end =" ")
name = input()


# Initilize the number of guess taken
guessTaken = 0

# Declare a random number between 1 to 20
number = random.randint(1, 20)
print("Well", name, "I am thinking a number between 1 to 20")

# Make a conditional that verifie the number of guess
for guessTaken in range(6):
    print("Take a guess")
    guess = input()
    guess = int(guess)

    # Verifie if guess is lower or higher or equal to number
    if guess < number:
        print("Your guess is too low!!!")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break

# Verifie if guess is equal to number what to do
if guess == number:
    guessTaken = str(guessTaken + 1)
    print("Good Job", name, "you win after", guessTaken, "guesses")

if guess != number:
    number = str(number)
    print("You're out of guess taken")
    print("Nope, the number was thinking of was:", number, ".")