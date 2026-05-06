# 10. Print the product of digits of a given number

def produt_of_digits(num):
    prod = 1
    while num > 0:
        digit = num % 10
        prod *= digit
        num = num // 10
        
    return prod

print(produt_of_digits(2222))