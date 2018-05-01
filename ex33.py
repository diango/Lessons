# Initialize one variable "i" and a list "numbers" 
i = 0
numbers = []

# Create a "while" loop to iterate over
while i < 6:
    print(f"At the top of i is {i}")
    # Append "i" to the list
    numbers.append(i)

    # Incremente the loop
    i = i + 1
    # Print the number in the list
    print("Numbers now: ", numbers)
    print("At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
