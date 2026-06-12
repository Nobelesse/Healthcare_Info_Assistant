import streamlit as st

st.set_page_config(
    page_title="Healthcare Info Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title(
    "🏥 Healthcare Info Assistant"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Modules", "6")

with col2:
    st.metric("AI Model", "Gemini")

with col3:
    st.metric("Version", "3.0")

st.markdown("---")

st.markdown("""
### Features

✅ Healthcare Chatbot

✅ Symptom Checker

✅ Disease Information

✅ Health Tips

✅ Medical Report Analysis

✅ Chat Export
            
✅ Medical Knowledge Base

---

### Disclaimer

This application provides educational information only.

Always consult qualified healthcare professionals for diagnosis and treatment.
""")