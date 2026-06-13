import streamlit as st

from utils.session_manager import initialize_session
from utils.database import initialize_database
from utils.ui import load_css

# ------------------------------------
# Page Configuration
# ------------------------------------

st.set_page_config(
    page_title="Healthcare Information Assistant",
    page_icon="🏥",
    layout="wide"
)

# ------------------------------------
# Initialization
# ------------------------------------

initialize_session()
initialize_database()
load_css()

# ------------------------------------
# Sidebar
# ------------------------------------

with st.sidebar:

    try:
        st.image(
            "assets/logo.png",
            width=150
        )
    except:
        pass

    st.title(
        "🏥 Healthcare Assistant"
    )

    st.markdown("---")

    st.info(
        "AI-Powered Healthcare Information Platform"
    )

    st.markdown(
        "Version 6.0"
    )

# ------------------------------------
# Header Section
# ------------------------------------

st.markdown(
    """
    <div class='main-header'>
        🏥 Healthcare Information Assistant
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-header'>
        AI-Powered Healthcare Education Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------
# Analytics Cards
# ------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Questions Asked",
        st.session_state.get(
            "questions_asked",
            0
        )
    )

with col2:

    st.metric(
        "Reports Analyzed",
        st.session_state.get(
            "reports_analyzed",
            0
        )
    )

with col3:

    st.metric(
        "Documents Uploaded",
        st.session_state.get(
            "documents_uploaded",
            0
        )
    )

with col4:

    st.metric(
        "KB Searches",
        st.session_state.get(
            "kb_searches",
            0
        )
    )

st.markdown("---")

# ------------------------------------
# Feature Overview
# ------------------------------------

st.subheader("🚀 Platform Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:

    st.success("AI Healthcare Chatbot")

    st.success("Symptom Checker")

    st.success("Disease Information")

    st.success("Health Tips Generator")

with feature_col2:

    st.success("PDF Report Analysis")

    st.success("Medical Knowledge Base (RAG)")

    st.success("Analytics Dashboard")

    st.success("Feedback System")

st.markdown("---")

# ------------------------------------
# About Project
# ------------------------------------

st.subheader("📚 About This Project")

st.write(
    """
    Healthcare Information Assistant is an AI-powered platform
    designed to provide educational healthcare information,
    document analysis, symptom guidance, and knowledge retrieval
    using Retrieval-Augmented Generation (RAG).

    Technologies Used:

    • Python 3.12

    • Streamlit

    • Google Gemini API

    • SQLite Database

    • Scikit-Learn

    • Plotly Analytics

    • PDF Processing
    """
)

st.markdown("---")

# ------------------------------------
# Disclaimer
# ------------------------------------

st.warning(
    """
    Medical Disclaimer:

    This application is intended for educational and informational
    purposes only. It does not provide medical diagnosis,
    treatment recommendations, or emergency healthcare services.

    Always consult a qualified healthcare professional for
    medical concerns.
    """
)

# ------------------------------------
# Footer
# ------------------------------------

st.markdown(
    """
    <div class='footer'>
        Healthcare Information Assistant © 2026
    </div>
    """,
    unsafe_allow_html=True
)