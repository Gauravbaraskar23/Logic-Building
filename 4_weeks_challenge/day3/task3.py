# Task 3: Generator countdown(n).
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# for x in countdown(3):
#     print(x)

g = countdown(3)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # if comment out raise StopIteration