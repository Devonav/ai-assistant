# AI Assistant (FastAPI + GPT-4)

This is a simple AI-powered virtual assistant using FastAPI, OpenAI GPT-4, and Docker.

## Features
- Conversational interface (text-based)
- GPT-4 powered responses
- Basic memory system
- Simple skill integrations (e.g., weather)

## Run with Docker

```bash
docker build -t ai-assistant .
docker run -e OPENAI_API_KEY=your_key_here -p 8000:8000 ai-assistant
Example request
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me the weather in Orlando"}'

