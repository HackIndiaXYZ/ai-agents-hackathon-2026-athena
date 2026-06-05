# agents/teacher.py
import google.generativeai as genai

from config import GEMINI_API_KEY
from rag.retrieval import retrieve_context

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_teacher(question):

    context = retrieve_context(question)

    prompt = f"""
You are TutorPilot AI, a multilingual STEM tutor.

Use the provided context to answer the student's question.

If the answer is in the context:
- explain clearly
- use simple language
- provide examples when possible

If the answer is not found:
- answer using your STEM knowledge
- clearly explain the concept

Context:
{context}

Student Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text