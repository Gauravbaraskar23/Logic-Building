# 3. Take day and month and check if it forms a valid calendar date (ignoring leap years).
def is_valid_calendar_date(day, month ):
    if month > 12 or day > 31 or day < 1 or month <1:
        return False
    elif month == 2 and day > 28 :
        return False
    elif month in [2, 4, 6, 9, 11] and  day > 30:
        return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and  day > 31:
        return False
    else:
        return True
        
day = int(input("Enter day: "))
month = int(input("Enter month: "))    
print(is_valid_calendar_date(day, month))