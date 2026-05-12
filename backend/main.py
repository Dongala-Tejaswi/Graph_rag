from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
file="C:\\AIML\\graph_rag\\data\\sample.txt"

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.retrieval.retriever import retrieve_context
from backend.llm.llm_engine import generate_answer

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Graph RAG Running"}

@app.post("/ask")
def ask_question(request: QueryRequest):

    context = retrieve_context(request.query)

    answer = generate_answer(
        request.query,
        context
    )

    return {
        "query": request.query,
        "context": context,
        "answer": answer
    }