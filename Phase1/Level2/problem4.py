# 4. Check if one of two given numbers is a multiple of the other.

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

if num1 % num2 == 0:
    print("num1 is multiple of num2.")
else:
    print("num1 is not a multiple of num2")
    
if num2 % num1 == 0:
    print("But num2 is a multiple of num1.")
else:
    print("num2 is not a multiple of num1")
    
if num2 % num1 == 0 and num1 % num2 == 0:
    print("Both are the multiple of each other.")
