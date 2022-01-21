#We’ve already seen a few python functions such as print and input, but now we’re going to dive into writing our own functions. To get started, we’ll write a function that takes in a number and squares it:

def square(x):
    return x * x



#Notice how we use the def keyword to indicate we’re defining a function, that we’re taking in a single input called x and that we use the return keyword to indicate what the function’s output should be.

#We can then “call” this function just as we’ve called other ones: using parentheses:
for i in range(10):
    print(f"The square of {i} is {square(i)}")

""" Output:
The square of 0 is 0
The square of 1 is 1
The square of 2 is 4
The square of 3 is 9
The square of 4 is 16
The square of 5 is 25
The square of 6 is 36
The square of 7 is 49
The square of 8 is 64
The square of 9 is 81
"""
