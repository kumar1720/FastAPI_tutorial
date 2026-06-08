# Path parameter - used to identify specific resource.
# CRUD (create, retrive, update, delete).
# Path - used to provide metadata,validation rules, & 
# documentation hints for path parameters in api endpoints.
# path() - improves readbility.
# HTTPException - used to return custom HTTP error responses.
# 
from fastapi import FastAPI, Path, HTTPException
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
def view_patient(patient_id: str = Path(..., description= "ID of patient in DB", example='P001')):
    # load all the patient data and return specfic data of a patient based on patiend_id.
    data= load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error' : 'Patient not found.'}, if data not found
    raise HTTPException(status_code= 404, detail= 'Patient not Found')
# HTTPException - It is a special built-in exception in FastAPI used to return
#               custom HTTP error responses when something goes wrong in your API
# read about HTTP status code.
#  HTTP Status Code - It is a 3-digit number returned by web server(FastAPI)
#                     to indicate the result of a client's request
# 2** - Successfull (eg. 200 ok - Standard success, 201 created - resource created, 204 No content - success, but no data returned.)
# 3** - Redirection - Further action need to be taken(start with 300).
# 4** - Client Error(somthing wrong with the request from clint, eg. 400 - bad request, 401 - unauthorized, 403 - forbidden, 404 - not found)
# 5** - server error (somthing went wrong on server side. eg.  500 - internal server error, 502- bad gateway, 503- service unavailable)