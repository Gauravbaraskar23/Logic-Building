# 8. Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.
char  = input("Enter character: ")
alphabets1 = 'abcdefghijklmABCDEFGHIJKLM'
alphabets2 = 'nopqrstuvwxyzNOPQRSTUVWXYZ'

if char in alphabets1:
    print(f"{char} is lies between a-m")

if char in alphabets2:
    print(f"{char} is lies between n-z")

