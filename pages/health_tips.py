import streamlit as st

from utils.ai_engine import get_ai_response

st.title("💡 Health Tips Generator")

topic = st.selectbox(
    "Choose Topic",
    [
        "General Health",
        "Weight Loss",
        "Heart Health",
        "Diabetes Prevention",
        "Mental Wellness",
        "Healthy Eating",
        "Exercise"
    ]
)

if st.button("Generate Tips"):

    prompt = f"""
    Generate practical health tips about:

    {topic}

    Use bullet points.
    """

    tips = get_ai_response(prompt)

    st.markdown(tips)