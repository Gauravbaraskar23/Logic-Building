# total(*args) returns the sum of any number of numbers. show(**kwargs) prints each key and value. Test total(), total(1, 2, 3) and show(name="Gaurav", city="Indore").

def total_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


print(total_sum(1,2,3))

def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show(name="Gaurav", city="Indore")

x = 10
def f():
    print(x)
    x = 5
f()