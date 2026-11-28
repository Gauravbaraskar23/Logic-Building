class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"
    
class Developer(Person):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
        
    def greet(self):
        message = super().greet()
        return f"{message} and I code in {self.language}"

p = Person("Gaurav")
d = Developer("Gaurav", "Python")

print(p.greet())
print(d.greet())

print(isinstance(d, Person))