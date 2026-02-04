from fastapi import FastAPI
from api import calculator_router

app = FastAPI(title="Calculator Services UN SE Night", description="This is a set of web services to handle aritmetic operations", version="0.1.1")

@app.get('/healthcheck')
def healthcheck():
    return {"message": "Services are up."}

app.include_router(calculator_router)