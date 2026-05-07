# 1. Count the number of digits in a given number.

def count_no_of_digits(num):
    count_digit = 0
    while num > 0:
        digits = num % 10
        count_digit += 1 
        num = num //10
    return count_digit

print(count_no_of_digits(45559))
print(count_no_of_digits(45559435))
print(count_no_of_digits(4524675))