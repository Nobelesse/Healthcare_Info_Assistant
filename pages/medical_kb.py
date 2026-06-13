import streamlit as st

from utils.pdf_reader import extract_pdf_text
from utils.chunker import chunk_text
from utils.vector_store import SimpleVectorStore
from utils.ai_engine import answer_rag_question

st.title("📚 Medical Knowledge Base (RAG)")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    full_text = ""

    for file in uploaded_files:

        full_text += extract_pdf_text(file)

    chunks = chunk_text(full_text)

    store = SimpleVectorStore()

    store.build(chunks)

    st.session_state["vector_store"] = store

    st.success(
        f"Indexed {len(chunks)} chunks."
    )

if "vector_store" in st.session_state:

    question = st.text_input(
        "Ask a question"
    )

    if st.button("Search"):

        store = st.session_state[
            "vector_store"
        ]

        retrieved = store.search(
        question,
        top_k=3
        )

    context = "\n\n".join(
        [
            item["chunk"]
            for item in retrieved
        ]
    )

    answer = answer_rag_question(
        context,
        question
    )

    st.markdown(answer)

    st.subheader(
        "Retrieved Sources"
    )

    for i, item in enumerate(
        retrieved,
        start=1
    ):

        with st.expander(
            f"Chunk {i} | Score: {item['score']:.3f}"
        ):

            st.write(
                item["chunk"]
            )