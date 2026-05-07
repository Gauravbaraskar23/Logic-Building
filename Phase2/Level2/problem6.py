# 6. Check if a number is a perfect number.

def perfect_number(num):
    divisor_sum = 0
    for i in range(1, num):
        if num%i == 0:
            # print(i)
            divisor_sum += i
            # print(divisor_sum)
    if num == divisor_sum:
        return True
    else:
        return False

print(perfect_number(6))
print(perfect_number(28))
print(perfect_number(11))
print(perfect_number(496))
print(perfect_number(125))