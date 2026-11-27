# Task 2: @logger decorator that works on functions with any arguments, using *args and **kwargs.
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
def add(a,b):
    return a + b

print(add(2,3))
print(add.__name__)
