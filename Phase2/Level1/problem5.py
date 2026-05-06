# 5. Print the table of a given number (n × 1 to n × 10).

def table_of_n(n):
    for i in range(1,11):
        print(n, 'x', i, '=', n*i)
    
# n = int(input("Enter a number: "))
# table_of_n(2)
# table_of_n(18)
table_of_n(15)