"""
Using lambda function with list comprehensions can result in strange behavior.
Here we define list of lambda functions that should multiply given number by integers from range [0, 9].
Instead, the multiplier is last value of given range, in this case 9.
The reason behind this is x variable used in lambda is accessed lazily, when the lambda is
invoked, not initialized
"""


multiply_functions = [lambda a: a * x for x in range(10)]


for func in multiply_functions:
    print(func(5))  # expected: 0, 5, 10, 15...
