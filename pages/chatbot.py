import streamlit as st

from utils.ai_engine import get_ai_response
from utils.emergency import check_emergency
from utils.export_chat import create_chat_pdf

st.title("🤖 Healthcare Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input(
    "Ask your healthcare question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    if check_emergency(prompt):
        emergency_msg = """
⚠️ Potential emergency detected.

Please seek immediate medical attention or contact emergency services.
"""

        with st.chat_message("assistant"):
            st.markdown(emergency_msg)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": emergency_msg
            }
        )

    else:

        answer = get_ai_response(prompt)

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
if st.session_state.messages:

    txt_content = ""

    for msg in st.session_state.messages:

        txt_content += (
            f"{msg['role'].upper()}: "
            f"{msg['content']}\n\n"
        )

    st.download_button(
        label="⬇ Download TXT",
        data=txt_content,
        file_name="chat_history.txt",
        mime="text/plain"
    )

    pdf_file = create_chat_pdf(
        st.session_state.messages
    )

    st.download_button(
        label="⬇ Download PDF",
        data=pdf_file,
        file_name="chat_history.pdf",
        mime="application/pdf"
    )