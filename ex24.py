# Print an introductory text
print("Let's practice everything.")
print('You\'d need to know \'bout espaces with \\ that do:')
print('\n newlines and \t tabs')

# Make a variable with poem as name
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.from
"""

# Make aline of separation for better visualization
print("----------" * 3)
print(poem)
print("----------" * 3)

# Make a simple calculation
five = 10 - 2 + 3 - 6
print(f"It should be five {five}")

# Define a function
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars,crates

# Create one variable "start_point" with 10000 as value
start_point = 10000

# Make "beans, jars and crates as aargument" of secret_formula
beans, jars, crates = secret_formula(start_point)

# Remember that this is a another to format a string
print("With a starting of: {}".format(start_point))

# It's just like with an f"" format string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates")

start_point = start_point / 10
