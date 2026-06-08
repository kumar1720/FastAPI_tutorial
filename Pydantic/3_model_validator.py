# Model Validator - The model_validator decorator in Pydantic is used to define custom validation logic for an entire model.
#                   It allows you to perform validation on the model as a whole, rather than just individual fields. 
#                   This can be useful when you need to validate the relationships between different fields 
#                   or when you want to enforce certain constraints that involve multiple fields.
# The model_validator decorator is applied to a method within the Pydantic model class, and it takes a single argument,
# which is the model instance being validated. The decorated method should return the validated model instance or raise
# a ValueError if the validation fails. 
# This allows you to ensure that the data in your Pydantic models meets specific criteria and adheres to your
# application's requirements at the model level, rather than just at the field level.     
# validating the relationships between different fields or when you want to enforce certain constraints that involve multiple fields.         
# In the above code, we define a Pydantic model called Patient with various fields such as name, email, age, weight, 
# married, allergies, and contact_details. We use the model_validator decorator to create custom validation logic for
# the entire model. The validate_emergency_contact method checks if the patient's age is greater than 60 and if so,
# it ensures that an emergency contact is provided in the contact_details field. If the validation fails, it raises a 
#ValueError with an appropriate message. 
# Finally, we create an instance of the Patient model using a dictionary of patient information and call
# the update_patient_data function to demonstrate how the data is validated and parsed by Pydantic, including the 
# custom validation logic defined in the model validator.          
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)