# 4. Check whether a given integer is single-digit, double-digit, or multi-digit.

num = int(input("Enter number: "))

hundreds  = num % 1000
tens = num % 100
ones = num % 10


if len(str(num)) == len(str(ones)):
    print("Given number is sigle digit.")

elif len(str(num)) == len(str(tens)):
    print("Given number is double digit.")


elif len(str(num)) == len(str(hundreds)):
    print("Given number is 3-digit.")
    
else:
    print("Given number is multi digit.")
