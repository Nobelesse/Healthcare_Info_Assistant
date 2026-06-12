import streamlit as st

from utils.ai_engine import get_ai_response

st.title("📚 Disease Information")

disease = st.text_input(
    "Enter disease name"
)

if st.button("Get Information"):

    if disease:

        prompt = f"""
        Explain {disease}

        Include:

        - Overview
        - Symptoms
        - Causes
        - Prevention
        - Treatment Overview

        Educational purposes only.
        """

        response = get_ai_response(prompt)

        st.markdown(response)