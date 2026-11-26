# Reverse a string 3 ways (slicing, reversed, a loop).


# def reverse_string(text):
    # return text[::-1]
    
    
# def reverse_string(text):
    # return text[::-1]
    # reverse_txt = "".join(reversed(text))
    # return reverse_txt


def reverse_string(text):
    n = len(text)
    
    for i in range(n-1, -1, -1):
        print(text[i], end='')
    
        
        



text = "Python"
reverse_string(text)
# print(reverse_string(text))