
# 2. If the sides form a valid triangle, determine whether it is equilateral, isosceles, or
# scalene.

a = int(input("enter side a: "))
b = int(input("enter side b: "))
c = int(input("enter side c: "))

if a == b == c:
    print("This is a Equilateral triangle.")
elif a == b != c or a==c != b or a != b == c:
    print("This is a Isosceles triangle.")
else:
    print("Scalene Triangle.")