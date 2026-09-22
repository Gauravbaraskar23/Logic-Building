# 8. Check if a number is prime or not.


def is_prime_or_not(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
        
    return True

print(is_prime_or_not(11))
print(is_prime_or_not(17))
print(is_prime_or_not(23))
print(is_prime_or_not(15))
print(is_prime_or_not(29))
print(is_prime_or_not(4))
