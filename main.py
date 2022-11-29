from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Werden Sie gesund."}

