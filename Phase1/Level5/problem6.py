# 6. Take three numbers and check if they are in geometric progression.
def geometric_progression(a, b, c):
    if  b/a == c/b:
        return "It is GP." 
    elif (b * b) == (a * c):
        return "It is GP."
    else:
        return False

a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))
c = int(input("Enter third no.: "))

print(geometric_progression(a, b, c))
