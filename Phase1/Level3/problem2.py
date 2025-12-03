
# 2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or
# neither.

# num = int(input("Enter number: "))
num = int(input("Enter number: "))

hundreds  = num // 100
tens = (num // 10) %10
ones = num % 10
if tens > hundreds and tens > ones:
    print("Middle digit is largest.")

elif tens < hundreds and tens < ones:
    print("Middle digit is smallest.")

elif tens > hundreds and tens < ones:
    print("Middle digit is larger than first digit but smaller than last digit.")


elif tens < hundreds and tens > ones:
    print("Middle digit is smaller than first digit but larger than last digit.")

else:
    print("Middle digit neither larger nor smaller.")