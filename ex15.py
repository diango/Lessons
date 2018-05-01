# # Import the function "argv" from "sys" module 
# from sys import argv

# # Declare that "script and filename" herit argv function
# script, filename = argv

# # Declare a var "txt" when you open the filename
# txt = open(filename)

# # Print the name of filename
# print(f"Here's your file {filename}")
# # Print the text inside of filename
# print(txt.read())

# # Print again the filename again
# print("Type the filename again:")
# # Ask user to type the name of the file
# file_again = input(">")

# # Open to the screen the filename contenu
# txt_again = open(file_again)
# # Print the filename in the screen
# print(txt_again.read()) 

from sys import argv
script, filename = argv

text = open(filename)

print(f"This is your file: {filename}")
print(text.read())

print("Type your filename again")
file_again = input("> ")

text_again = open(file_again)
print(text_again.read())






























