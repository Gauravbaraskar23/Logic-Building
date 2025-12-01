# 10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special
# character.

char =  input("Enter character: ")

if char.isdigit():
    print("A digit")
    
elif char.isupper():
    print("It's Uppercase")

elif char.islower():
    print("It's Lowercase")

else:
    print("It's a special charcter")