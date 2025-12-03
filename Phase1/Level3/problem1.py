# 1. Take a 3-digit number and check if all digits are distinct.
num = int(input("Enter number: "))

hundreds  = num // 100
tens = (num // 10) %10
ones = num % 10
if hundreds != tens and tens != ones and hundreds != ones:
    print("All digits are distinct")
else:
    print("All digits are not distinct")