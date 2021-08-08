"""
When using decorator, original function metadata, such name, docstring and signature
will be overridden by wrapping function
"""

from functools import wraps


def decorator(func):
    def wrapper(*args, **kwargs):
        # do something
        return func(*args, **kwargs)

    return wrapper


@decorator
def some_function(arg_1, arg_2):
    """
    :param arg_1:
    :param arg_2:
    :return:
    """
    # do something
    pass


print(some_function.__name__, "simple decorator")  # we want it to be some_function
print(some_function.__doc__)  # docs are lost :/

"""
Solution for this problem is using functools.wraps decorator on inner decorator's wrapper function.
This will preserve our decorated function metadata
"""


def better_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something
        return func(*args, **kwargs)

    return wrapper


@better_decorator
def some_function_correct_way(arg_1, arg_2):
    """

    :param arg_1:
    :param arg_2:
    :return:
    """
    # do something
    pass


print(some_function_correct_way.__name__, "decorator with functools.wraps")
print(some_function_correct_way.__doc__)
