from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import requests

from logggerrr import setup_logger

app = FastAPI()

logger = setup_logger('backend', 'backend.log')

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

        return {"summary": response.json()}
    
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
