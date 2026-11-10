
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from ai import ask_gemini
from pydantic import BaseModel, Field, field_validator
from fastapi.middleware.cors import CORSMiddleware

Conversations = {}

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins=[
          "http://127.0.0.1:5500",
          "http://localhost:5500"
     ],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

class ChatRequest(BaseModel):
    conversation_id: str = Field(min_length = 1)
    message: str = Field(min_length=2, max_length = 2000)
    username: str = Field(min_length = 1, max_length = 50)

    @field_validator("message")
    @classmethod
    def validate_message(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Message can't be empty or whitespace only.")

        return value

class ChatResponse(BaseModel):
    response: str
    status: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Create conversation if it doesn't exist
    if request.conversation_id not in Conversations:
        Conversations[request.conversation_id] = []

    # Add the NEW user message
    Conversations[request.conversation_id].append({
        "role": "user",
        "content": request.message
    })

    # Get the updated conversation
    history = Conversations[request.conversation_id]

    print("CURRENT HISTORY:", history)

    # Send updated history to Gemini
    try:
     answer = ask_gemini(history)

    except Exception as e:
        print("Gemini Server Error:", e)

    # Remove the unanswered user message
        history.pop()

        raise HTTPException(
            status_code = 502,
            detail = "AI service is temporarily unavailable. Please try again."
        )


    # Store Gemini's response
    Conversations[request.conversation_id].append({
        "role": "assistant",
        "content": answer
    })

    # Limit the conversation history to the last 20 messages

    if len(Conversations[request.conversation_id]) > 20:
        Conversations[request.conversation_id] = Conversations[request.conversation_id][-20:]

    # Return response to frontend
    return {
        "response": answer,
        "status": "success"
    }