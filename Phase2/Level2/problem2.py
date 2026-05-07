# 2. Print the reverse of a given number.

def reverse_number(num):
    num1 = []
    while num > 0:
        digits = num % 10
        print(digits)
        num1.append(digits)
        print(num1)
        
        num = num //10
    return num1

# print(reverse_number(123456))

# Or

def reverse_number1(num):
    rev_num = 0
    while num != 0:
        digits = num % 10
        # print(digits)
        rev_num = (rev_num* 10) + digits
        # print(rev_num)
        
        num = num //10
    return rev_num

print(reverse_number1(123456))
