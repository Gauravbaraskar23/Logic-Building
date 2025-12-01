# 10. Take a month number (1–12) and print the number of days in that month (ignore leap
# years).

month = int(input("Enter month number: "))

match month:
    case 1:
        print("No. of days is 31")
    case 2:
        print('No. of days is 28')
    case 3:
        print("No. of days is 31")
    case 4:
        print("No. of days 30")
    case 5:
        print("No. of days is 31")
    case 6:
        print("No. of days 30")
    case 7:
        print("No. of days is 31")
    case 8:
        print("No. of days 31")
    case 9:
        print("No. of days is 30")
    case 10:
        print("No. of days 31")
    case 11:
        print("No. of days is 30")
    case 12:
        print("No. of days 31")
    
    case _:
        print("Enter valid months.")
        