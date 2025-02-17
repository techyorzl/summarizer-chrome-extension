import torch
import json
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

with open('configs.json', 'r') as file:
    config = json.load(file)

try:
    summarizer = pipeline('summarization', model=config['model'])
except Exception as e:
    summarizer = None

class TextReq(BaseModel):
    text: str

@app.post("/generate_summary")
async def generate_summary(text: str):
    if not summarizer:
        raise RuntimeError("Model is not loaded properly!")
    
    try:
        text_len = len(text.split())
        max_tokens = int(max(0.3 * text_len, 150))

        summary = summarizer(text, max_length=max_tokens, min_length=int(max_tokens * 0.5), do_sample=False)
        return {"summary": summary[0]["summary_text"]}
    
    except Exception as e:
        return "Error generating summary."