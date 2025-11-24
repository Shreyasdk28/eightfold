import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

print("Available Gemini models that support generateContent:\n")
models = genai.list_models()
for m in models:
    if 'generateContent' in m.supported_generation_methods:
        print(f"Model: {m.name}")
        print(f"  Display Name: {m.display_name}")
        print(f"  Supported Methods: {m.supported_generation_methods}")
        print()
