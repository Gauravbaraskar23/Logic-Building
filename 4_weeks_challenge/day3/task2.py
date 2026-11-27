# Task 2: @logger decorator that works on functions with any arguments, using *args and **kwargs.
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a,b):
    return a + b

print(add(2,3))
print(add.__name__)
