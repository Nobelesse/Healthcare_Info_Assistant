import streamlit as st

from utils.pdf_reader import extract_pdf_text
from utils.ai_engine import analyze_medical_report

st.title("📄 Medical Report Analysis")

st.info(
    "Upload a medical PDF report for educational explanation."
)

uploaded_file = st.file_uploader(
    "Upload PDF Report",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading PDF..."):

        report_text = extract_pdf_text(
            uploaded_file
        )

    st.success("PDF Loaded Successfully")

    with st.expander("Extracted Text Preview"):

        st.text(
            report_text[:3000]
        )

    if st.button("Analyze Report"):

        with st.spinner(
            "Analyzing report..."
        ):

            analysis = analyze_medical_report(
                report_text
            )

            st.session_state.reports_analyzed += 1

            st.markdown(analysis)