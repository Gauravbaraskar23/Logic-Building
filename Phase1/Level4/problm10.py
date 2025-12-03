# 10. Take a password string and check basic rules (length ≥ 8 and contains at least one
# digit).

password = input("Enter a password: ")

if len(password) >= 8 :
    for char in password:
        if char.isdigit():
            print("Password is correct.")
            break
        