# 9. Take electricity units consumed and calculate the bill as per slabs (using if-else).

unit_consumed = int(input("Enter unit consumed by the user: "))

total_bill = 0

if unit_consumed <= 200 :
    total_bill = unit_consumed * 3.80
    print(total_bill)
elif 200 <unit_consumed <=300:
    total_bill = unit_consumed * 4.40
    print(total_bill)

elif 300 <unit_consumed <=400:
    total_bill = unit_consumed * 5.10
    print(total_bill)

else:
    total_bill = unit_consumed * 5.80
    print(total_bill)
