import streamlit as st

from utils.pdf_reader import extract_pdf_text
from utils.ai_engine import answer_document_question

st.title("📚 Medical Knowledge Base")

uploaded_files = st.file_uploader(
    "Upload Medical PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    combined_text = ""

    for file in uploaded_files:

        text = extract_pdf_text(file)

        combined_text += (
            f"\n\n--- DOCUMENT: {file.name} ---\n\n"
        )

        combined_text += text

    st.session_state["kb_text"] = combined_text

    st.success(
        f"{len(uploaded_files)} document(s) loaded."
    )

if "kb_text" in st.session_state:

    question = st.text_input(
        "Ask a question about uploaded documents"
    )

    if st.button("Search Knowledge Base"):

        with st.spinner("Analyzing documents..."):

            answer = answer_document_question(
                st.session_state["kb_text"],
                question
            )

        st.markdown(answer)