# 4. Find the sum of digits of a number.

def sum_of_digits(num):
    digit_sum = 0 
    while num > 0:
        digit = num % 10
        digit_sum += digit
        
        num = num // 10
    return digit_sum

num = 1298
print(sum_of_digits(num))        
print(sum_of_digits(12345))        
print(sum_of_digits(8754))        
print(sum_of_digits(12346789))        
        