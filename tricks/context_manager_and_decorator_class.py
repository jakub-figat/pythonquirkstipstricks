from contextlib import contextmanager, ContextDecorator
from functools import wraps
import time

"""
Both context managers and decorators are very convenient syntactic sugars available in Python.
And there's possibility to merge them into even more convenient functionality.
We can use contextlib.ContextDecorator to allow using context manager as decorator
Suppose that we have decorator that can measure a time that function takes to finish it's work
"""


def measure_time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        time_delta = time.time() - start_time
        print(f"Time: {time_delta:.2f}s")
        return result
    return wrapper


# Or as context manager

@contextmanager
def measure_time_context_manager():
    start_time = time.time()
    try:
        yield
    finally:
        time_delta = time.time() - start_time
        print(f"Time: {time_delta:.2f}s")


# Both context manager and decorator

class measure_time_context_decorator(ContextDecorator):

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        time_delta = time.time() - self.start_time
        print(f"Time: {time_delta:.2f}s")


# now we can use it both as context manager and decorator


def slow_function():
    return [num for num in range(10**7)]

