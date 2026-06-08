# Pydantic - Pydantic is a data validation(& data parsing) and settings management library for Python. It uses Python type
#            annotations tovalidate and parse data, making it easier to work with complex data structures. Pydantic provides
#             a powerful and flexible way to define data models, ensuring that the data conforms to the specified
#             types and constraints.   
#             It is commonly used in FastAPI to define request and response models, as well as to  validate and parse 
#             incoming data in API endpoints.      
# BaseModel - It is a base class provided by Pydantic that you can inherit from to create your own data models. It provides
#             built-in validation and parsing capabilities based on the type annotations you define in your model.
# EmailStr - It is a special type provided by Pydantic that validates whether a given string is a valid email address. 
#            It ensures that the string follows the standard email format.
# AnyUrl - It is a special type provided by Pydantic that validates whether a given string is a valid URL. 
#          It checks if the string follows the standard URL format, including the scheme (e.g., http, https), domain, and 
#          optional path and query parameters.
# Field - It is a function provided by Pydantic that allows you to define additional metadata and validation rules for fields
#         in your data model. You can use it to set constraints such as maximum length, minimum value, default values, and 
#         provide descriptions for documentation purposes.
# Optional - It is a type hinting feature from the typing module in Python that indicates that a value can either be of a 
#            specified type or None. 
# Annotated - It is a type hinting feature introduced in Python 3.9 that allows you to attach additional metadata to type 
#            annotations. In the context of Pydantic, you can use Annotated to provide extra information about a field, such as
#           validation rules or descriptions, while still maintaining the original type annotation for validation purposes.    
# In the above code, we define a Pydantic model called Patient with various fields such as name, email, linkedin_url, age, 
# weight, married, allergies, and contact_details. Each field is annotated with its respective type and additional metadata 
# using Field and Annotated. The update_patient_data function takes an instance of the Patient model and prints out some of 
# its attributes. Finally, we create an instance of the Patient model using a dictionary of patient information and call the 
# update_patient_data function to demonstrate how the data is validated and parsed by Pydantic.
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[Optional[bool], Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)