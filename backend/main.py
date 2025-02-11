from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from backend.logggerrr import setup_logger
from model.model_api import generate_summary

app = FastAPI()

logger = setup_logger('backend', 'backend.log')

class TextRequest(BaseModel):
    text: str

@app.post("/generate_summary")
async def summarize_text(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    try:
        summary = await generate_summary(request.text)
        return {"summary": summary}
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

