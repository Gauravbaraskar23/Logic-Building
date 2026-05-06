# 9. Take two dates (day and month) and determine which one comes first in the
# calendar.

def check_first_come_date(d1, m1, d2, m2):
    if d1 > 31 or m1 > 12 or m2 > 31 or d1 > 31:
        return False
    elif (m1 == 2 and d1 > 28) or (m2 == 2 and d2 > 28):
        return False
    elif m1 < m2:
        return "Date 1 comes first"
    elif m2 < m1:
        return "Date 2 comes first"
    else: 
        if d1 < d2:
            return "Date 1 comes first"
        elif d2 < d1:
            return "Date 2 comes first"
        else:
            return "Both dates are same"


d1 = int(input("Enter first date: "))
d2 = int(input("Enter second date: "))
m1 = int(input("Enter first month: "))
m2 = int(input("Enter second month: "))

print(check_first_come_date(d1, m1, d2, m2))