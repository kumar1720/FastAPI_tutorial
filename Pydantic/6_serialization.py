# Serialization - It is the process of converting a data structure or object into a format that can be easily stored 
#                or transmitted and later reconstructed. 
#                In Pydantic, you can serialize models to various formats such as JSON, dictionaries, or even custom formats.       
# In the above code, we define an Address model with fields for city, state, and pin. We then define a Patient model 
#that includes an Address field, allowing us to nest the Address model within the Patient model. We create an instance 
#of the Address model using a dictionary, and then create an instance of the Patient model that includes the Address instance.
# Finally, we use the model_dump method to convert the Patient model instance into a dictionary and print its type, 
# demonstrating how nested models work in Pydantic.    
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()
# temp = patient1.model_dump(include={'name', 'age'})
# temp = patient1.model_dump(exclude={'name', 'age'})
# temp = patient1.model_dump(include={'address': {'city', 'state'}})
# temp = patient1.model_dump(exclude={'address': {'pin'}})    
# temp = patient1.model_dump(exclude_unset=True) # only include fields that were explicitly set when creating the model instance
# temp = patient1.model_dump(exclude_defaults=True) # only include fields that have values different from their default values
# temp = patient1.model_dump(exclude_none=True) # only include fields that have non-None values   

print(temp)
print(type(temp))