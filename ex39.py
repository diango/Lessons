# Create a mapping of state to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# Create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "ML": "Jacksonville"
}

# Add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# Print out some cities
print("******" * 10)
print("NY State has:", cities["NY"])
print("OR State has:", cities["OR"])

# Print some states
print("--------" * 10)
print("Michigan abbreviation is:", states["Michigan"])
print("Florida abbreviation is:", states["Florida"])

# Do it by using the state then cities dict
print("-----------" * 10)
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Florida"]])


















