# 8. Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

temp = int(input("Enter Temperture: "))

if temp < 15:
    print("cold")

elif  30 >= temp >= 15:
    print("Warm")

else:
    print("Hot")