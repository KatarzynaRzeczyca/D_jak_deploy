# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.counter = 0

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.get("/method")
def root():
    return {"method": "GET"}

class GiveMeSomethingRq(BaseModel):
    name: str
    surename: str


class GiveMeSomethingResp(BaseModel):
    id: int
    patient: dict

class GiveMeSomethingRespPut(BaseModel):
    received: dict
    method: str = "PUT"

# @app.put("/method", response_model=GiveMeSomethingRespPut)
# def put_something(rq: GiveMeSomethingRq):
#     return GiveMeSomethingRespPut(received=rq.dict())

@app.delete("/method")
def root():
    return {"method": "DELETE"}

@app.post("/method")
def root():
    return {"method": "POST"}

@app.put("/method")
def root():
    return {"method": "PUT"}

@app.post("/patient", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
	app.counter += 1
	return GiveMeSomethingResp(id = app.counter, patient=rq.dict())