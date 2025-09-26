from pydantic import BaseModel,EmailStr,Field, model_validator
from typing import List, Dict, Any, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool =  Field(default=None)
    contact_details: Dict[str, str] =  Field(default=None)

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contacts:
            raise ValueError('Patients older than 60 must have emergency contact')
        return model



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
    "email":'abc@icici.com',
    "age": 30,
    "weight": 55.6,
    "contacts": {"phone": "911111111"},
}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
update_patient_data(patient1)
