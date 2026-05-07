# 3. Check if a number is a palindrome.
def is_palindrome(str1):
    str1 = str1.lower()
    str2 = str1[::-1]
    for i in range(len(str1)):
        if str1 == str2:
            return True
        else:
            return False
# n = input("Enter a string: ")

print(is_palindrome('Markram'))

# OR 
        
        
def is_palindrome(str1):
    str1 = str1.lower()
    n = len(str1)
    l = 0
    r = n-1
    for i in range(n):
        if str1[l] == str1[r]:
            # print(str1)
            l += 1
            r -= 1
            
        else:
            return False
    
    return True
            
# n = input("Enter a string: ")

print(is_palindrome('Markram'))
print(is_palindrome('Teacher'))