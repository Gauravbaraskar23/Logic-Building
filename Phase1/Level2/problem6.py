# 6. Check voting eligibility for a given age (18+).

age = int(input("Enter Age: "))

if 100 >= age >= 18:
    print("Eligible to vote.")
else:
    print("Not Eligible to vote.")