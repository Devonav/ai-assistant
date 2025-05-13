from fastapi import FastAPI, Request
from app.nlu import ask_openai
from app.skills import handle_weather
from app.memory import add_to_memory, get_similar

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Assistant is running"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")

    memory_context = get_similar(user_input)
    reply = ask_openai(user_input, context=memory_context)

    if "weather" in user_input.lower():
        reply += "\n" + handle_weather("Orlando")

    add_to_memory(user_input, reply)
    return {"response": reply}
