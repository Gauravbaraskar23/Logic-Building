# make_multiplier(n) returns a function, so double = make_multiplier(2) and double(5) gives 10.

def make_multiplier(n):
    def multiplier(x):
        return x * n
    
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
quadruple = make_multiplier(4)

print(double(5))
print(triple(5))
print(quadruple(5))
print(make_multiplier(10)(4))