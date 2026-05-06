# 7. Take a 3-digit number and check if the sum of the first and last digit equals the middle
# digit.

def check_valid_equation(a, b, c):
    if a + c == b:
        return True
    else:
        return False

a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))
c = int(input("Enter third no.: "))

print(check_valid_equation(a, b, c))
