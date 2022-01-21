#Loops are an incredibly important part of any programming language, and in Python, they come in two main forms: for loops and while loops. For now, we’ll focus on For Loops.

#For loops are used to iterate over a sequence of elements, performing some block of code (indented below) for each element in a sequence. For example, the following code will print out the numbers from 0 to 5:
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

""" Output:
0
1
2
3
4
5
"""

#We can condense this code using the python range function, which allows us to easily get a sequence of numbers. The following code gives the exact same result as our code from above:
for i in range(6):
    print(i)

""" Output:
0
1
2
3
4
5
"""

#This type of loop can work for any sequence! For example, if we wish to print each name in a list, we could write the code below:
# Create a list:
names = ["Harry", "Ron", "Hermione"]

# Print each name:
for name in names:
    print(name)

""" Output:
Harry
Ron
Hermione
"""

#We can get even more specific if we want, and loop through each character in a single name!
name = "Harry"
for char in name:
    print(char)

""" Output:
H
a
r
r
y
"""