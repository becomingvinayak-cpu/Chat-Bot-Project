
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

    # Find the newest USER message
    latest_user_index = None

    for i in range(len(history) - 1,
    -1, -1):
        if history[i]["role"] == "user":
            latest_user_index = i
            break

    if latest_user_index is None:
        raise ValueError("No user message found.")

    # Get the actual latest user message
    
    latest_message = history[latest_user_index]["content"]
    print("LATEST USER MESSAGE:", latest_message)

    # Everything before the latest user message is previous context
    
    previous_conversation = ""

    for message in history[:latest_user_index]: previous_conversation += (

        f"{message['role'].upper()}: "
                    f"{message['content']}\n"
    )

    prompt = f"""
You are a helpful AI assistant.

Previous conversation:
{previous_conversation}

Latest user message:
{latest_message}

Answer the latest user message
directly.
Use the previous conversation only
when it is relevant.
Do not treat the previous message as
the current question.
"""

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(

                model = "gemini-3.6-flash",
                contents = prompt
            )

            if not response.text:
                raise RuntimeError("Gemini returned an empty response.")

            return response.text

        except Exception as e:

            print(f"Error on attempt {attempt + 1}: {e}")

            if attempt < max_retries -1:
               time.sleep(2 ** attempt)

            else:
                raise