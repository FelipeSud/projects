# Lambda functions provide another way to create functions in python. For example, if we want to define the same square function we did earlier, we can write:
square = lambda x: x * x

# Where the input is to the left of the : and the output is on the right.

# This can be useful when we don’t want to write a whole separate function for a single, small use. For example, if we want to sort some objects where it’s not clear at first how to sort them. Imagine we have a list of people, but with names and houses instead of just names that we wish to sort:
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

""" Output:
[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]
"""




#While this does work, we’ve had to write an entire function that we’re only using once, we can make our code more readable by using a lambda function:
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)

""" Output:
[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]
"""