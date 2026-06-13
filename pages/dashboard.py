import streamlit as st

st.title("📊 Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Questions Asked",
        st.session_state.get(
            "questions_asked",
            0
        )
    )

    st.metric(
        "Reports Analyzed",
        st.session_state.get(
            "reports_analyzed",
            0
        )
    )

with col2:

    st.metric(
        "Documents Uploaded",
        st.session_state.get(
            "documents_uploaded",
            0
        )
    )

    st.metric(
        "Knowledge Base Searches",
        st.session_state.get(
            "kb_searches",
            0
        )
    )

st.markdown("---")

st.info(
    "Analytics are stored for the current session."
)