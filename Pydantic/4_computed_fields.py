# Computed Fields - Computed fields are a powerful feature in Pydantic that allow you to define fields in your data model
#                   that are computed based on other fields.
#                   These fields are not directly provided by the user but are derived from the values of other fields 
#                   in the model. Computed fields can be useful for performing calculations, transformations, 
#                   or any logic that depends on the values of other fields. 
# To define a computed field in Pydantic, you can use the @computed_field decorator along with a property method. 
# The property method should return the computed value based on the other fields in the model. When you access the 
# computed field, Pydantic will automatically call the property method and return the computed value. 
# This allows you to encapsulate complex logic within your Pydantic models and keep your code clean and organized. 
# Computed fields can be used for various purposes, such as calculating derived attributes, formatting data, or performing 
# any necessary transformations based on the existing fields in the model. 
# In the above code, we define a Pydantic model called Patient with various fields such as name, email, age, weight, height,
# married, allergies, and contact_details. We use the @computed_field decorator to define a computed field called bmi, 
# which calculates the Body Mass Index (BMI) based on the weight and height fields. The bmi property method performs the 
# calculation and returns the computed value. Finally, we create an instance of the Patient model using a dictionary of 
#patient information and call the update_patient_data function to demonstrate how the data is validated and parsed by 
# Pydantic, including the computed field for BMI.
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 
print("STARTED")

update_patient_data(patient1)