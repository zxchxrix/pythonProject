from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

    # return f'Student name: {name}, ID: {school_id}, GPA: {float(random.randint(0, gpa))}'


alex = Student('Alex', '4623477', 3.4)
print(alex.name)
print(alex.school_id)
print(alex)

michelle = Student('Michelle', '7773335', 2.7)
print(michelle)
