# 9. Take two angles of a triangle and compute the third angle.

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))

res = side1 + side2  
if res < 180:
    side3 = 180 - res
    print(side3)
else:
    print("Please! Enter a valid angles.")

# or


# res =180 - (side1 + side2)  

# print(res)
