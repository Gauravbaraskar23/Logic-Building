# 1. Take a character and check if it is a letter, a digit, or neither.

char  = input("Enter a character: ")

if char.isdigit():
    print("A digit")

elif char.isalpha():
    print("A Letter")

else:
    print("Neither a letter nor a digit")
    