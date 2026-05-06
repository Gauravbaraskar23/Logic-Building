# 9. Print the factorial of a given number.

def factorial_of_n(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

print(factorial_of_n(5))
print(factorial_of_n(3))
print(factorial_of_n(6))