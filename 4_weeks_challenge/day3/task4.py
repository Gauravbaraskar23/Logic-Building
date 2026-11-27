# Task 4: Generator fibonacci(limit) that yields Fibonacci numbers below limit.
def fibonacci(limit):
    f1 = 0
    f2 = 1
    while f1 < limit:
        yield f1
        f1 , f2 = f2, f1 + f2


print(list(fibonacci(50)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

