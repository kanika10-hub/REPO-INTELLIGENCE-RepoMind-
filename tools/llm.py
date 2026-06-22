import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_llm(prompt: str, max_retries: int = 5):
    """
    Simple wrapper for Gemini calls with retry logic.
    Used by all agents.
    """

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            print(f"[LLM Retry {attempt + 1}] {e}")
            time.sleep(3)

    return "Gemini unavailable."