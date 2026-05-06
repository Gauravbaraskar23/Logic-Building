# 8. Take an integer (1–9999) and check if the sum of its digits is greater than the product
# of its digits.

def check_number_is_equal_or_not(n):
    sum = 0
    product = 1
    if  n >= 9999:
        return False
    else:
        for i in range(0,n):
            
            sum = sum + n%10
            product = product * n
            n = n//10
        
    if sum > product:
        return True
    else:
        return False           

n = int(input("Enter an integer between 1-9999: "))
print(check_number_is_equal_or_not(n))
    
    