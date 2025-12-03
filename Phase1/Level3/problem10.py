# 10. Check whether a number is a perfect square (without using the square root function).

# n = int(input("Enter number: "))

# if num % 10 == 2 or num % 10 == 3 or num % 10 == 7 or num % 10 == 8 :
#     print("Given number is not a perfect square.")
# else:
#     print("Given number is a perfect square.")

def isPerfectSquare(n):
    i = 1
    while n > 0:
        n -= i
        i += 2
    return n == 0
n = int(input("Enter number: "))
if isPerfectSquare(n):
    print("Given number is a perfect square.")
else:
    print("No")