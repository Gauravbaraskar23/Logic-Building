# 5. Check if a number is a multiple of 7 or ends with 7.

num = int(input("Enter number: "))

if num % 7 == 0 or num % 10 == 7:
    print("Number is a multiple of 7 or ends with 7.")
else:
    print("number is neither a multiple of 7 nor ends with 7.")