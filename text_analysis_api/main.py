# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, logging
from fastapi.middleware.cors import CORSMiddleware

logging.set_verbosity_error()


app = FastAPI(title="Text Analysis API")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

# Hugging Face pipelines
sentiment_analyzer = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")

class TextInput(BaseModel):
    text: str

# Sentiment analyzer
@app.post("/sentiment")
def analyze_sentiment(input: TextInput):
    result = sentiment_analyzer(input.text)[0]
    return {
        "label": result['label'],
        "score": result['score']
    }

# Summarizer
@app.post("/summary")
def summarize_text(input: TextInput):
    summary_result = summarizer(
        input.text, 
        max_length=50,   
        min_length=25,
        do_sample=False
    )
    return {
        "summary": summary_result[0]['summary_text']
    }