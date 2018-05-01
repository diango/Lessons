# from sys import argv
# script, filename = argv

# print(f"We're going to erase {filename}.")
# print("If you don't want that, hit CTRL-C (^C).")
# print("If you do wnat that, hit RETURN.")

# print("?")

# print("Opening the file:")
# target = open(filename, "w")

# print("Truncate the file, GoodBye")
# target.truncate()

# print("Now I am going to ask you three lines.")
# line1 = input("Line1: ")
# line2 = input("Line2: ")
# line3 = input("Line3: ")

# print("I am going to write this to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# print("And finally, we cloe it.")
# target.close()


from sys import argv
script, filename = argv

print(f"Your filename is: {filename}")

print("Opening filename")
target = open(filename, "w")

print("truncate filename")
target.truncate()

print("I gonna ask to add three lines")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I am going to write this in the file")

target.write(f"{line1}\n{line2}\n{line3}")

print("I gonna close it here")
target.close()


































