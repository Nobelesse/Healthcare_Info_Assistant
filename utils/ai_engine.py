import streamlit as st
import google.generativeai as genai

from utils.prompts import (
    SYSTEM_PROMPT,
    REPORT_ANALYSIS_PROMPT,
    DOCUMENT_QA_PROMPT
)

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

def analyze_medical_report(report_text):

    prompt = f"""
    {REPORT_ANALYSIS_PROMPT}

    {report_text}
    """

    response = model.generate_content(prompt)

    return response.text

def answer_document_question(document_text, question):

    prompt = f"""
    {DOCUMENT_QA_PROMPT}

    {document_text}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text