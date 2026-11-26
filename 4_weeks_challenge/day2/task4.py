# Write one function with a required argument, a default argument, *args and **kwargs, in the correct order. Call it 3 different ways.

def func(name, role="student" ,*args, **kwargs):
    print(f"name: {name}")
    print(f"role: {role}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    
func("Gaurav")
func("Gaurav", "Developer", "Python", "Django")
func("Gaurav", "Developer", "Python",city="Indore", age=22)