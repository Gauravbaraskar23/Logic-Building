# 5. Take three numbers and check if they are in arithmetic progression.
def arithmetic_progression(a, b, c):
    if( b-a) == (c-b):
        return True 
    elif (2 * b) == (a + c):
        return True
    else:
        return False

a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))
c = int(input("Enter third no.: "))

print(arithmetic_progression(a, b, c))
