from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from ai import ask_gemini
from pydantic import BaseModel, Field

Conversations = {}

app = FastAPI()

class ChatRequest(BaseModel):
    conversation_id: str
    message: str = Field(min_length=3)
    username: str

class ChatResponse(BaseModel):
    response: str
    status: str

@app.post("/chat", response_model = ChatResponse)
def chat(request: ChatRequest):

    if request.conversation_id not in Conversations:

         Conversations[request.conversation_id] = []

         Conversations[request.conversation_id].append(
              {
                   "role": "user",
                   "content": request.message
              }
         )

    try:
            history = Conversations[request.conversation_id]
            answer = ask_gemini(history)
            Conversations[request.conversation_id].append({
                 "role": "assistant",
                 "content": answer})
            
    except Exception as e:
         print("Gemini Error:", e)
         raise HTTPException(
              status_code=500,
              detail="Failed to get response from Gemini"
         )