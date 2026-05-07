# 5. Check if a number is an Armstrong number.
# An Armstrong number (also called a Narcissistic number) is a number that is equal 
# to the sum of its digits raised to the power of the total number of digits.

def count_no_of_digits(num):
    
    count_digit = 0
    while num > 0:
        digits = num % 10
        count_digit += 1 
        num = num //10
    return count_digit

# print(count_no_of_digits(45559))

def armstrong_number(num):
    total_digits = count_no_of_digits(num)
    original_num = num
    # print(total_digits)
    countdigit = 0
    sum_digit = 0
    while num > 0:
        digit = num% 10
        prod_digit =  digit ** total_digits
        print(prod_digit)
        sum_digit += prod_digit
        print(sum_digit)
        
        num = num//10
    
    if original_num == sum_digit:
        return True
    else:
        return False
    
print(armstrong_number(153))
print(armstrong_number(370))
print(armstrong_number(8208))
print(armstrong_number(123))

    
        


