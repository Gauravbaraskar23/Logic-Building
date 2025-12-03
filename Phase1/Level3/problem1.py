# 1. Take a 3-digit number and check if all digits are distinct.
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))

if num1 != num2 and num1 !=  num3 and num2 != num3:
    print("All digits are distinct")
else:
    print("All digits are not distinct")