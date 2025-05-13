# Minimal memory system (in-memory list + FAISS placeholder)
memory = []

def add_to_memory(question: str, answer: str):
    memory.append((question, answer))

def get_similar(query: str) -> str:
    # Simulate "context" retrieval (can integrate FAISS later)
    return memory[-1][1] if memory else ""
