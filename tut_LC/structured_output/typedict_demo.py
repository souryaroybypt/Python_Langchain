from typing import TypedDict

class Person(TypedDict):
    name: str
    age:int

p1: Person = {'name':"Abc",'age':20}
print(p1)