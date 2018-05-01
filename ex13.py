from sys import argv
# Read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second is:", second)
print("The third variable is:", third)


age = input("How old are you? ")
color = input("What color do yo prefer? ")
choes = input("What is your prefer mark? ")
language = input("Do you speak english? ")
hacking = input("Do you know what is hacking?(Yes/No) ")
sport = input("Which sport do you like? ")


from sys import argv
script, age, color, choes, language, hacking, sport = argv

print("The name of the script is:", script)
print("You're", age, "old")
print("You prefer", color, "color")
print("Your preference is", language)
print("You know nothing about hacking", hacking)
print("You prefer", sport, "like sport")



