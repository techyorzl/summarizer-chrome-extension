import torch
import json
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

with open('configs.json', 'r') as file:
    config = json.load(file)

summarizer = pipeline("summarization", model=config['model'])

class TextReq(BaseModel):
    text: str

@app.post("/generate_summary")
def generate_summary(request: TextReq):
    text_len = len(request.text.split())
    max_tokens = int(max(0.3 * text_len, 150))


    summary = summarizer(request.text, max_length= max_tokens, min_length = int(max_tokens * 0.5), do_sample=False)
    return {"summary": summary[0]["summary_text"]}