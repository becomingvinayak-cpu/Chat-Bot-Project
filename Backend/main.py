from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from ai import ask_gemini
from pydantic import BaseModel, Field

app = FastAPI()

class ChatRequest(BaseModel):
    message: str = Field(min_length=3)
    username: str

class ChatResponse(BaseModel):
    response: str
    status: str

@app.post("/chat", response_model = ChatResponse)
def chat(request: ChatRequest):
    try:
            answer = ask_gemini(request.message)
            return {
                "response": answer,
                "status": "success"
            }
    except Exception as e:
         raise HTTPException(
              status_code=500,
              detail="Failed to get response from Gemini"
         )