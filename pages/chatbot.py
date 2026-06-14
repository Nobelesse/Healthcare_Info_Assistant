import streamlit as st

from utils.ai_engine import get_ai_response
from utils.emergency import check_emergency
from utils.export_chat import create_chat_pdf
from utils.history import save_query

from streamlit_mic_recorder import mic_recorder

from utils.speech_handler import save_audio


# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------

defaults = {
    "questions_asked": 0,
    "chat_history": [],
    "messages": []
}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value


# --------------------------------------------------
# Page Title
# --------------------------------------------------

st.title("🤖 Healthcare Chatbot")


# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


# --------------------------------------------------
# Voice Input Section
# --------------------------------------------------

st.markdown("---")

st.subheader("🎤 Voice Input")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹ Stop Recording",
    just_once=True,
    use_container_width=True
)

if audio:

    try:

        audio_path = save_audio(
            audio["bytes"]
        )

        st.success(
            "Voice recording captured successfully."
        )

        st.audio(
            audio["bytes"]
        )

        st.info(
            "Phase 7A currently records audio only. Speech-to-text will be added in Phase 7B."
        )

    except Exception as e:

        st.error(
            f"Audio Error: {str(e)}"
        )


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

prompt = st.chat_input(
    "Ask a healthcare question..."
)


# --------------------------------------------------
# Process User Message
# --------------------------------------------------

if prompt:

    save_query(prompt)

    st.session_state.questions_asked += 1

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # Emergency Detection

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


# --------------------------------------------------
# Export Chat
# --------------------------------------------------

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