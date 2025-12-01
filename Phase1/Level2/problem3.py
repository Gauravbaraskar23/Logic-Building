# 3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).

marks = float(int(input('Enter marks: ')))

if 100 >= marks >= 80:
    print("Grade A")
elif 80 > marks>= 65:
    print("Grade B")
elif 65 > marks >= 55:
    print("Grade C")
elif 55 > marks >= 45:
    print("Grade D")
    
elif 45 > marks >= 33:
    print("Grade E") 
elif 33 > marks >= 0:
    print("Grade F")

else:
    print("Please! Enter a valid marks.")