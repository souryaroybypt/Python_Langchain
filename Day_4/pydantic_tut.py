from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Any, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int =  Field(gt=0,lt=100)
    weight: float = Field(gt=0,strict=True)
    married: bool = Field(default = None)
    allergies: Optional[List[str]] = Field(default=None,max_length=5) 
    contacts: Dict[str, Any]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("data inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("data updated")


patient_info = {
    "name": "Abc",
    "email":'abc@gmail.com',
    "linkedin_url":"http://linknedin.com/abc",
    "age": 30,
    "weight": 55.6,
    "contacts": {"phone": "911111111"},
}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
update_patient_data(patient1)
