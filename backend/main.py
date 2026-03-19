from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_sql, explain_result
from db import run_query

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    sql = generate_sql(query.question)
    
    result = run_query(sql)
    
    explanation = explain_result(query.question, result)
    
    return {
        "sql": sql,
        "result": result,
        "explanation": explanation
    }