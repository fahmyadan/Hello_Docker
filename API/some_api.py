from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path

import logging
logger = logging.getLogger()


app = FastAPI()

class User(BaseModel):
    name: str

class Nums(BaseModel):

    integer: str

@app.post("/greet_user")
async def greet_user(request: dict):
    first_name, age = request['first'], request['age']
         
    try:
        greeting = f'Hello Mr {first_name}, you are {age} years old \n IT WORKS'
        return greeting
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))


