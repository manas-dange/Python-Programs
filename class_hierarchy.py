class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self,name,age,rollno,stream):
        super().__init__(name,age)
        self.rollno=rollno
        self.stream=stream
s=student("Manas","18","122","CSE")
print(f"Name: {s.name}, Age: {s.age}, Roll No: {s.rollno}, Stream: {s.stream}")
