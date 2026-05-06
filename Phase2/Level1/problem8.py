# 8. Print the sum of all odd numbers up to n.

def sum_of_n_odd(n):
    odd_sum = 0
    for i in range(1, n+1):
        if i%2 != 0:
            odd_sum += i
            
    return odd_sum

print(sum_of_n_odd(10))