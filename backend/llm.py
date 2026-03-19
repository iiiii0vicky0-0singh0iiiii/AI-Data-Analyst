from openai import OpenAI
from schema import schema

client = OpenAI(api_key="YOUR_API_KEY")

def generate_sql(question):
    prompt = f"""
    Convert this natural language to SQL.
    
    Schema:
    {schema}
    
    Question:
    {question}
    
    Only return SQL query.
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()


def explain_result(question, result):
    prompt = f"""
    Question: {question}
    Result: {result}
    
    Explain in simple English.
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content