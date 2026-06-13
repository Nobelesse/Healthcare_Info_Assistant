import streamlit as st


def initialize_session():

    defaults = {
        "questions_asked": 0,
        "reports_analyzed": 0,
        "documents_uploaded": 0,
        "kb_searches": 0,
        "history": []
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value