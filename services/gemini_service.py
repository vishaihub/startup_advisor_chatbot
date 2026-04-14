import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME
import logging

genai.configure(api_key=GEMINI_API_KEY)
def get_gemini_response(prompt):
    try:
        response = genai.GenerativeModel(MODEL_NAME).generate_content(
            contents=prompt
        )
        return response.text

    except Exception as e:
        logging.error(f"Gemini API Error: {str(e)}")
        return "⚠️ Something went wrong. Please try again."