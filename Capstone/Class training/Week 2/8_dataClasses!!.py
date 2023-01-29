from dataclasses import dataclass


@dataclass
class Student:
    name = str
    school_id = str
    gpa = float


alex = Student()
print(alex.name)
print(alex.school_id)
print(alex)

michelle = Student()
print(michelle)
