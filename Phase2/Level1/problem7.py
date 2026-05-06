# 7. Print the sum of all even numbers up to n.

def sum_of_n_even(n):
    even_sum = 0
    for i in range(1, n+1):
        if i%2 == 0:
            even_sum += i
            
    return even_sum

print(sum_of_n_even(10))