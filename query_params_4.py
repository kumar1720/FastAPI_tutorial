# Query Parameter - it is a optional key-value pair appended 
# at the end of URL, used for operations like Filtering, sorting,
# searching, and pagination, without altering the endpoint
# path itself.
# Eg - /patients?city= Delhi & sort_by= age
#  The ? marks is the start of query params
# Each params is the key-value pair
# Multiple params are separated by &.
# In this case:
#             * city = delhi is a query parameter of filtering
#              * sort_by=age is a query parameter for sorting
# Query()  is a utility function provided by FastAPI to declare, validate, and 
# document query parameters in your API endpoints. It also allow us to
# set default value, Enforce validation rules, Add metadat description, title, example
from fastapi import FastAPI, Path, HTTPException, Query
import json
app= FastAPI()
# load json data
def load_data():
    with open('patients.json', 'r') as f:
        data= json.load(f)
    return data    

@app.get("/")
def hello():
    return{'message' : 'Patient Management System API'}
@app.get('/about')
def about():
    return {'message' : 'API to manage patient records.'}
@app.get('/view')
def view():
    data = load_data()
    return data
@app.get('/patient/{patient_id}')
#  using path func.
def view_patient(patient_id: str = Path(..., description= "ID of patient in DB", example='P001')):
    # load all the patient.
    data= load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error' : 'Patient not found.'}
    raise HTTPException(status_code= 404, detail= 'Patient not Found')
#  applying query params.
# sort patient -> Query()
#                  |     |
#              sort_by   order
#                |           |
#            based on wt,    ASC, DSC
#            ht, bmi
@app.get('/sort')
#  using query() func.
def sort_patient(sort_by: str=Query(..., description='Sort on the basis of height, wt or bmi'), order: str= Query('asc',description= 'sort by asc or dsc.')):
    valid_field= ['height', 'weight', 'bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f'Invalid field selected from{valid_field}')
    
    if order not in ['asc', 'dsc']:
        raise HTTPException(status_code=400,detail='Invalid Order selected.')
    
    data=load_data()

    sort_order= True if order == 'desc' else False
    
    sorted_data= sorted(data.values(),key= lambda x: x.get(sort_by,0), reverse= sort_order)
    return sorted_data