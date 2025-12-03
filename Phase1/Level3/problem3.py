# 3. Take a 4-digit number and check if the first and last digits are equal.
# while True:
#     user_input = input("4-digt number is: ")
#     if user_input.isdigit() and len(user_input) == 4 :
#         num = int(user_input)
#         break
#     else:
#         print("Please enter 4-digit number!!!!")

num = int(input("Enter number: "))
if 1000 <= num <= 9999:
        
    thousands = num // 1000
    hundreds  = (num // 100)
    tens = (num // 10) %10
    ones = num % 10

    if thousands == ones:
        print("First and last digits are equal.")
    else:
        print("First and last digits are not equal.")

else:
    print("Please! Enter a 4-digit number.")