class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
    
    def __str__(self):
        return f"Student(name={self.name}, average={self.average()})"
    
s1 = Student("Gaurav", [80,90,70])
print(s1.average())
print(s1)

s2 = Student("Amit", [])
print(s2.average())
print(s2)
  