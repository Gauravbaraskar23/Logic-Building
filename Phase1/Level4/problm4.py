# 4. Take 24-hour time (hours and minutes) and print whether it is AM or PM.
time_str =(input("Enter time: "))
hours = int(time_str.split(':')[0])

if 0 < hours <=11:
    print("AM")

elif 12 <= hours <=23:
    print("PM")

else:
    print("Enter valid time")

