from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Def Name'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10, default=6, description='A decimal representing cgpa of student')

new_student = {'age':21,'email':'abc@gmail.com'}

s1 = Student(**new_student)

student_dict = dict(s1)

print(s1,type(s1))
print(student_dict['age'])

student_json = s1.model_dump_json()
print(student_json)