# 10. Take a year and print the corresponding century (e.g., “19th century”, “20th century”)

def check_century(year):
    if  1900 >= year >= 1801:
        return "19th Century"
    elif 2000 >= year >= 1901:
        return "20th Century"
    else:
        return "There is no  19th or 20 th century"

year = int(input("Enter Year: "))
print(check_century(year))