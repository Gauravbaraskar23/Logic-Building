# make_counter() returns a function that increases and returns a count on each call. Use nonlocal. Then create two counters and check that they don't share state.

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = make_counter()
c2 = make_counter()

print(c1())
print(c1())
print(c2())
print(c1())
print(c1())
print(c2())
print(c1())