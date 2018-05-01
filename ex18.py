def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} and arg2: {arg2}")

def print_two(arg1, arg2):
    print(f"arg1: {arg1} and arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")

print_two("Mamadou", "Badiane")
print_two("Mamadou", "Badiane")
print_one("Vivement")
print_none()

