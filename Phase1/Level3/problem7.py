# 7. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
amount = int(input("Enter amount: "))  
    
if amount % 100 == 0:
    print("Amount can be evenly divided into 2000, 500, and 100 currency notes.")
    
else:    
    print("Amount cannot be evenly divided into 2000, 500, and 100 currency notes.")
