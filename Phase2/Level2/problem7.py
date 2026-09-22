# 7. Print all prime numbers between 1 and 100.



def print_n_prime_num(num1, num2):
    for num in range(num1+1, num2+1):
        is_prime = True
        
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                is_prime = False
            break
        
        
        if is_prime:
            print(num, end=' ')
        
    

print_n_prime_num(1, 100)
# print(print_n_prime_num(17))