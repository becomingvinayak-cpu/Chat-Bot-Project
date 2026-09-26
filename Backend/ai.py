
import os
import time

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
        conversation_text += (f"{message['role']}:{message['content']}\n"
        )

    max_retries = 3

    for attempt in range(max_retries):
        try:

            response = client.models.generate_content(
                model = 'gemini-3.6-flash',
                contents=conversation_text
            )
            return response.text

        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise e