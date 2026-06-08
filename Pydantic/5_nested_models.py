# Nested Models in Pydantic allow you to define complex data structures by embedding one model within another. 
# This is particularly useful when you have related data that can be logically grouped together. 
# For example, you might have a Patient model that includes an Address model as a nested field. 
# This allows you to organize your data more effectively and maintain a clear structure.  
# Benefits of Nested Models:
#                          Better organization of related data (e.g., vitals, address, insurance)    
#                          Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)
#                          Readability: Easier for developers and API consumers to understand
#                          Validation: Nested models are validated automatically—no extra work needed
# In the above code, we define an Address model with fields for city, state, and pin. We then define a Patient model 
# that includes an Address field, allowing us to nest the Address model within the Patient model. We create an instance 
# of the Address model using a dictionary, and then create an instance of the Patient model that includes the Address instance. 
# Finally, we use the model_dump method to convert the Patient model instance into a dictionary and print its type, 
# demonstrating how nested models work in Pydantic.    
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()

print(type(temp))























# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed