import streamlit as st

from utils.session_manager import (
    initialize_session
)

initialize_session()

st.set_page_config(
    page_title="Healthcare Info Assistant",
    page_icon="🏥",
    layout="wide"
)

with st.sidebar:

    st.title(
        "🏥 Healthcare Assistant"
    )

    st.markdown("---")

    st.info(
        "AI-powered Healthcare Information Platform"
    )

    st.markdown(
        "Version 4.0"
    )

st.title(
    "🏥 Healthcare Info Assistant"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Questions Asked",
        st.session_state.questions_asked
    )

with col2:

    st.metric(
        "Reports Analyzed",
        st.session_state.reports_analyzed
    )

st.markdown("---")

st.markdown("""
### Features

✅ Healthcare Chatbot

✅ Symptom Checker

✅ Disease Information

✅ Health Tips

✅ PDF Medical Report Analysis

✅ Knowledge Base (RAG)

✅ Analytics Dashboard

✅ Search History

✅ Feedback System

---

### Disclaimer

This application provides educational healthcare information only.

It does not provide medical diagnosis or treatment.
""")