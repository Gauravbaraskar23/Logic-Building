# 2. Take three numbers and check if they can form a Pythagorean triplet.

def pythogorean_triplet(a, b, c):
    if a*a + b*b == c*c:
         
        return "Given numbers form pythagorean triplets"
    else:
        return "Not are triplets."

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

print(pythogorean_triplet(a, b, c))