# Write one function with a required argument, a default argument, *args and **kwargs, in the correct order. Call it 3 different ways.

def func(normal, *args, **kwargs):
    print(f'Default argument is : {normal}')
    
    print(f"positional arguments are : {args}")
    print(f"Keyword arguments are : {kwargs}")

func(2.5,3,4,5,6,6, name="Gaurav", city="Indore", age=22)