from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    email: str
    course: str

student = Student(
    name="Rahul",
    age="25",
    email="rahul@gmail.com",
    course="Python"
)

print(student)
print(student.name)
print(student.age)