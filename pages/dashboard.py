import streamlit as st
import plotly.express as px

st.title("📊 Analytics Dashboard")

questions = st.session_state.get(
    "questions_asked",
    0
)

reports = st.session_state.get(
    "reports_analyzed",
    0
)

documents = st.session_state.get(
    "documents_uploaded",
    0
)

searches = st.session_state.get(
    "kb_searches",
    0
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Questions Asked",
        questions
    )

    st.metric(
        "Reports Analyzed",
        reports
    )

with col2:

    st.metric(
        "Documents Uploaded",
        documents
    )

    st.metric(
        "KB Searches",
        searches
    )

chart_data = {
    "Category": [
        "Questions",
        "Reports",
        "Documents",
        "KB Searches"
    ],
    "Count": [
        questions,
        reports,
        documents,
        searches
    ]
}

fig = px.bar(
    chart_data,
    x="Category",
    y="Count",
    title="Usage Analytics"
)

st.plotly_chart(
    fig,
    use_container_width=True
)