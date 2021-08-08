"""
To fix this, we can bound list comprehension variable to lambda's scope
by defining it as a default argument.
"""

multiply_functions = [lambda a, x=x: a * x for x in range(10)]


for func in multiply_functions:
    print(func(5))  # expected: 0, 5, 10, 15
