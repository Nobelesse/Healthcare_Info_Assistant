import streamlit as st

from utils.ai_engine import get_ai_response
from utils.emergency import check_emergency

st.title("🩺 Symptom Checker")

symptoms = st.text_area(
    "Enter your symptoms",
    placeholder="Example: fever, headache, fatigue"
)

if st.button("Analyze Symptoms"):

    if symptoms:

        if check_emergency(symptoms):

            st.error(
                "Potential emergency detected. Seek immediate medical attention."
            )

        else:

            prompt = f"""
            User Symptoms:

            {symptoms}

            Provide:

            1. Possible conditions
            2. General explanation
            3. Self-care tips
            4. When to consult a doctor

            Do not diagnose.
            """

            result = get_ai_response(prompt)

            st.markdown(result)