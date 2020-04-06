# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.get("/method")
def root():
    return {"method": "GET"}

class GiveMeSomethingRq(BaseModel):
    first_key: str


class GiveMeSomethingResp(BaseModel):
    received: dict
    method: str = "POST"

class GiveMeSomethingRespPut(BaseModel):
    received: dict
    method: str = "PUT"


# @app.post("/method", response_model=GiveMeSomethingResp)
# def receive_something(rq: GiveMeSomethingRq):
#     return GiveMeSomethingResp(received=rq.dict())

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