# 8. Take a weekday number (1–7) and determine if it is a weekday or weekend.

weekday_num = int(input("Weekday number : "))

if weekday_num == 1 or weekday_num == 2 or weekday_num == 3 or weekday_num == 4:
    print("Today is a weekday")

elif weekday_num == 5 or weekday_num == 6 or weekday_num == 7:
    print('Today is a Weekend')

else:
    print("Plaese! Enter a valid week day number")