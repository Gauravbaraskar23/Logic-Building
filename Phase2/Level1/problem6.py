# 6. Print the sum of first n natural numbers.

def sum_of_natural_num(n):
    natural_sum = 0
    for i in range(1,n+1):
        natural_sum = natural_sum + i
    return natural_sum

n = int(input("Enter n number: "))
print(sum_of_natural_num(n))