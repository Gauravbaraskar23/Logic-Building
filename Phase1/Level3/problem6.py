# 6. Take coordinates (x, y) and determine which quadrant the point lies in.
x = int(input("Enter x coordinte: "))
y = int(input("Enter y coordinte: "))

if  x > 0 and y > 0:
    print("Points lies in first quadrant.")

elif x > 0 and y< 0:
    print("Points lies in second quadrant.")
    
elif x < 0 and y > 0:
    print("Points lies in third quadrant.")

else:
    print("Points lies in fourth quadrant.")
