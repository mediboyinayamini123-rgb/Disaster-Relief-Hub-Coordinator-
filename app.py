from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from orchestration.workflow import run_disaster_workflow
from agents.matcher_agent import restock_warehouse



app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class EmergencyRequest(BaseModel):
    message: str



@app.post("/analyze")
def analyze_emergency(request: EmergencyRequest):

    result = run_disaster_workflow(request.message)

    return result



@app.post("/restock")
def restock():

    return restock_warehouse()
