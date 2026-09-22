import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

client = genai.Client(api_key=api_key)

def ask_gemini(history):
    conversation_text = ""

    for message in history:
        conversation_text +=f"{message['role']}:{message['content']}\n"

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = conversation_text
    )

    return response.text