from pydantic import BaseModel,EmailStr,Field, field_validator
from typing import List, Dict, Any, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool =  Field(default=None)
    contact_details: Dict[str, str] =  Field(default=None)

    @field_validator('email') # custom validator
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid email")
        return value
    
    @field_validator('name') # transforms fields if needed
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age shud be b/w 0 & 100')


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
    "weight": 55.6
}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
update_patient_data(patient1)
