from fastapi import FastAPI
app=FastAPI()

"""
To run for development not production (alow for all 0.0.0.0) :
uvicorn main:app --reload --host 0.0.0.0 --port 8080
URL ==> http://localhost:8080/welcome
"""

@app.get("/welcome")
def welcome():
    return {
    "message": "Hello World!"
    }

