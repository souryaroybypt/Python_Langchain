from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, logging

logging.set_verbosity_error()

sentiment_analyzer = pipeline("sentiment-analysis")

app = FastAPI()

#input schema
class TextInput(BaseModel):
    text: str

# POST endpoint
@app.post("/analyze")
def analyze_sentiment(input: TextInput):
    result = sentiment_analyzer(input.text)[0]
    return {
        "label": result['label'],
        "score": result['score']
    }