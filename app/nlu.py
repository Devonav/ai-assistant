import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(prompt: str, context="") -> str:
    messages = [
        {"role": "system", "content": context or "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content
