import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# 1. Define the Data Contract (DTO)
class ChatRequest(BaseModel):
    prompt: str
    page_content: Optional[str] = None # We will use this in the next phase

app = FastAPI(title="Magma Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Magma Core Online"}

# 2. The Chat Logic
@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    print(f"Received prompt: {request.prompt}")
    
    # SIMULATION: Pretend we are calling OpenAI (Wait 1s)
    time.sleep(1)
    
    # Simple echo logic for now
    ai_response = f"Magma AI received: '{request.prompt}'"
    
    return {
        "response": ai_response,
        "usage": {"tokens": len(request.prompt.split())}
    }
