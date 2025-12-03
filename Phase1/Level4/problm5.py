# 5. Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

income = input('Income: ')
amount = int(income.split('L')[0])
age = int(input("Age: "))

if 100 >= age > 18 and amount > 5:
    print("Eligible for tax.")
else:
    print("not eligible")
