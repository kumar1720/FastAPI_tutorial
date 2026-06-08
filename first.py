 # creating first fastapi
# step:
# 1 - create virtual env (python -m venv myenv)
# 2- activate myenv (source myenv/bin/activate)
# pip install fastapi uvicorn, pydantic.
#  3- import and create app object
# 4- run (uvicorn first:app --reload)
# 5- http://127.0.0.1:8000/about - for about request
# 6- http://127.0.0.1:8000/docs - for seeing docs.
from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def hello():
    return{'message' : 'Hello world'}
@app.get('/about')
def about():
    return {'message' : 'Learning FastAPI.'}