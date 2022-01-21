#STRINGS
#Orderes: Yes | Mutable: No
name = 'Harry'
print(name[0])
print(name[1])


#LISTS
#A Python list allows you to store any variable types. We create a list using square brackets and commas, as shown below. Similarly to strings, we can print an entire list, or some individual elements. We can also add elements to a list using append, and sort a list using sort
#Ordere: Yes | Mutable: Yes
# This is a Python comment
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Sort the list:
names.sort()
# Print the new list:
print(names)


#TUPLES
#Tuples are generally used when you need to store just two or three values together, such as the x and y values for a point. In Python code, we use parentheses:
#Ordered: Yes | Mutable: No
point = (12.5, 10.6)

#SETS
#Sets are different from lists and tuples in that they are unordered. They are also different because while you can have two or more of the same elements within a list/tuple, a set will only store each value once. We can define an empty set using the set function. We can then use add and remove to add and remove elements from that set, and the len function to find the set’s size. Note that the len function works on all sequences in python. Also note that despite adding 4 and 3 to the set twice, each item can only appear once in a set.
#Ordered: No | Mutable: N/A
# Create an empty set:
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")

""" This is a python multi-line comment:
Output:
{1, 3, 4}
The set has 3 elements.
"""

#DICTIONARIES
#Python Dictionaries or dicts, will be especially useful in this course. A dictionary is a set of key-value pairs, where each key has a corresponding value, just like in a dictionary, each word (the key) has a corresponding definition (the value). In Python, we use curly brackets to contain a dictionary, and colons to indicate keys and values. For example:
#Ordered: No | Mutable: Yes
# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "Gryffindor"
# Print out Hermione's House:
print(houses["Hermione"])

""" Output:
Gryffindor
Gryffindor
"""