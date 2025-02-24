from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_API_URL = "http://model:5000"

class TextRequest(BaseModel):
    text: str

@app.post("/generate_summary")
async def summarize_text(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    try:
        response = requests.post(f"{MODEL_API_URL}/generate_summary", json={"text": request.text})
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Model server error")

        return response.json()
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
