# field_validator - It is a decorator provided by Pydantic that allows you to define custom validation logic for specific 
#                  fields in your data model.
#                   It is used to create custom validation rules that go beyond the built-in validation provided by Pydantic.
#                   You can use field_validator to implement complex validation logic, such as checking the format of a string,
#                   validating the range of a number, or enforcing specific constraints on a field's value. 
#                   The field_validator decorator is applied to a method within the Pydantic model class, and it takes the name
#                   of the field to be validated as an argument. 
# The decorated method should return the validated value or raise a ValueError if the validation fails. 
# This allows you to ensure that the data in your Pydantic models meets specific criteria and adheres to 
# your application's requirements. 
# In the above code, we define a Pydantic model called Patient with various fields such as name, email, age, weight, 
# married, allergies, and contact_details. 
# We use the field_validator decorator to create custom validation logic for the email, name, and age fields. 
# The email_validator method checks if the email domain is valid, the transform_name method transforms the name to uppercase,
# and the validate_age method checks if the age is within a specified range. 
# Finally, we create an instance of the Patient model using a dictionary of patient information and call 
# the update_patient_data function to demonstrate how the data is validated and parsed by Pydantic, including the custom
# validation logic defined in the field validators.
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)