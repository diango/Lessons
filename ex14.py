# from sys import argv

# script, user_name = argv
# prompt = ">"
# user_name = input()

# print(f"Hi {user_name}, I'm the {script} script.")
# print("I would like to ask you a few questions.")
# print(f"Do you like me {user_name}")
# like = input(prompt)

# print(f"Where do you live {user_name}")
# live = input(prompt)

# print(f"What kind of computer do you have {user_name}")
# computer = input(prompt)

# print(f"""
# So alright you said {like} about me.
# You live in {live}, No sure where that is
# And You have a {computer} computer. Nice 
# """)


from sys import argv

script, firstName, lastName = argv
prompt = ">>>"

print("Hi {} {}, I'm the {} script".format(firstName, lastName, script))
print("I wish to answer some questions....")
print("Do you like to travel the world? ")
like = input(prompt)

print("What is your favorite destination? ")
destination = input(prompt)

print("Do you care to be solely in the world? ")
alone = input(prompt)

print("Espagne or France or USA Or Russia which destination do you prefer? ")
preference = input(prompt)

print(f""" 
Alright, so you said: travel the world {like}.
Your favorite destination is {destination}.
To be alone: {alone}.
And your favorite destination is {preference}
""")




























