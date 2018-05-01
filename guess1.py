import random
print("*****----***** WELCOME THE BIGGEST GUESSING GAME *****------*****")

guessTaken = 0

print("What is your name buddy?", end=" ")
name = input()
print("You have only 05 guess to try:", name)

number = random.randint(1, 100)

for guessTaken in range(5):
    print("Take a guess")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print("You win after", guessTaken, "guess")

if guess != number:
    number = str(number)
    print("You are out of the range 05")
    print("The number I was thinking of was:", number, ".")