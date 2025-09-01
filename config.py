import os
from dotenv import load_dotenv
import google.generativeai as genai

# ---------------------
# Load environment
# ---------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY is missing. Please set it in .env file.")
else:
    print("✅ GEMINI_API_KEY loaded")

# ---------------------
# Configure Gemini
# ---------------------
genai.configure(api_key=api_key)

# Central place for model name
MODEL_NAME = "gemini-1.5-flash"

# Quick test
if __name__ == "__main__":
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content("Hello! Testing Gemini config.")
    print("🤖 Gemini says:", response.text)
