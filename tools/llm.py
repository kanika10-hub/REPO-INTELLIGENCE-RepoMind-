import time

from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_llm(prompt):
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                #gemini-2.5-flash-lite
                #gemini-2.0-flash
            contents=prompt
        )

            return response.text
   
        except Exception as e:
            print(f"Retry {attempt+1}: {e}")
            time.sleep(3)

    return "Gemini unavailable."