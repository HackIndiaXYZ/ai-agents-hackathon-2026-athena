# agents/quiz_generator.py
import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_quiz(topic, difficulty="medium", num_questions=5):

    prompt = f"""
Generate {num_questions} multiple-choice STEM questions.

Topic: {topic}
Difficulty: {difficulty}

Do NOT reveal the answers.

Format:

Q1:
Question

A) ...
B) ...
C) ...
D) ...

Q2:
...
"""

    response = model.generate_content(prompt)

    return response.text