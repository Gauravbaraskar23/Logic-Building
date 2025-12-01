# 5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good
# Evening”, or “Good Night”.

hours = int(input("Enter hours:"))

if 11 >= hours > 1:
    print("Good Morning!")
elif 17 > hours >= 12:
    print("Good Afternoon!")

elif 23 > hours >= 17:
    print("Good Evening!")

elif 24 > hours >=  23:
    print("Good Night!")

else:
    print("Enter a valid hours!")