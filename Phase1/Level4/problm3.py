# 3. Take three numbers and print the median value (neither maximum nor minimum).

num1 = int(input("Numm1: "))
num2 = int(input("Numm2: "))
num3 = int(input("num3: "))
median = []

median.append(num1)
median.append(num2)
median.append(num3)

median.sort()
print("The median value is: ",median[1])


