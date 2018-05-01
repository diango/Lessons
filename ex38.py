# Crete a variable "ten_things" 
ten_things = "Apples Oranges crows Telephone Light Sugar"

# Print a phrase of exclamation
print("Wait there are not 10 things in that list. Let's fix that.")

# Split "ten_things" and give it to a variable stuff
stuff = ten_things.split(' ')
# Declare a list "more_stuff" containing 8 items
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana",
            "Girl", "Boy"]

# Create a while loop where length stuff is different to 10
while len(stuff) != 10:
    # Use the function pop() to add items to "next_one"
    next_one = more_stuff.pop()
    # Print the result of the last add
    print("Adding: ", next_one)
    # Append the items to next_one
    stuff.append(next_one)
    # Print the length of items in my "stuff" variable
    print(f"There are {len(stuff)} items now.")

print("------******----" * 3)

print("there we go: ", stuff)
print("Let's do some things with stuff.")

print("-------**********------" * 3)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)
print(" ".join(stuff))
print(" # ".join(stuff[3:5]))