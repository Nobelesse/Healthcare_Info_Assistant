import streamlit as st
import google.generativeai as genai

from utils.prompts import SYSTEM_PROMPT

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def get_ai_response(user_query):

    prompt = f"""
    {SYSTEM_PROMPT}

    User Question:
    {user_query}
    """

    response = model.generate_content(prompt)

    return response.text