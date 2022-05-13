from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    query_string: str

@app.post("/query")
def my_endpoint(request: PredictionRequest):
    sentiment_model = pipeline("sentiment-analysis")
    sentiment_query_sentence = request.query_string
    sentiment = sentiment_model(sentiment_query_sentence)
    return f"Sentiment test: {sentiment_query_sentence} == {sentiment}"
    
@app.get("/health")
def health():
    return "Service is online"