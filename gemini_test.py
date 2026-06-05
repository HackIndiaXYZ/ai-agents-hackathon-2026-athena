# gemini_test.py
import google.generativeai as genai
from config import GEMINI_API_KEY

print("KEY:", GEMINI_API_KEY[:10])

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Say hello")

print(response.text)
