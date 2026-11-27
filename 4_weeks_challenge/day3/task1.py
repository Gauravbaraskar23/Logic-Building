# Task 1: @timer decorator. Print how long the function took, and return the original result.
import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds.")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))
# slow_sum took 0.03s
# 499999500000