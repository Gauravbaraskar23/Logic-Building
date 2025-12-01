# 7. Take two numbers and determine whether both are even, both are odd, or one is
# even and one is odd.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")

elif num1 % 2 == 0 and num2 % 2 != 0:
    print("num1 is even but num2 is odd.")
    
elif num2 % 2 == 0 and num1 % 2 != 0:
    print("num2 is even but num1 is odd.")
    
else:
    print("Both are odd")