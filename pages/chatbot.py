import streamlit as st

from utils.ai_engine import get_ai_response
from utils.emergency import check_emergency
from utils.export_chat import create_chat_pdf
from utils.history import save_query

from streamlit_mic_recorder import mic_recorder

from utils.speech_handler import (
    save_audio,
    speech_to_text,
    text_to_speech
)

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
# Voice Assistant
# --------------------------------------------------

voice_text = ""

st.markdown("---")

st.subheader("🎤 Voice Assistant")

audio = mic_recorder(
    start_prompt="🎤 Speak",
    stop_prompt="⏹ Stop",
    just_once=True,
    use_container_width=True
)

if audio:

    try:

        audio_path = save_audio(
            audio["bytes"]
        )

        with st.spinner(
            "Converting speech to text..."
        ):

            voice_text = speech_to_text(
                audio_path
            )

        st.success(
            "Speech recognized successfully."
        )

        st.info(
            f"📝 {voice_text}"
        )

    except Exception as e:

        st.error(
            f"Voice Error: {str(e)}"
        )


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

typed_prompt = st.chat_input(
    "Ask a healthcare question..."
)

prompt = None

if voice_text:

    prompt = voice_text

elif typed_prompt:

    prompt = typed_prompt


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

    # --------------------------------------------------
    # Emergency Detection
    # --------------------------------------------------

    if check_emergency(prompt):

        emergency_msg = """
⚠️ Potential emergency detected.

Please seek immediate medical attention or contact emergency services.
"""

        with st.chat_message("assistant"):

            st.markdown(emergency_msg)

        emergency_audio = text_to_speech(
            "Potential emergency detected. Please seek immediate medical attention."
        )

        st.audio(
            emergency_audio,
            format="audio/mp3"
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": emergency_msg
            }
        )

    else:

        with st.spinner(
            "Generating response..."
        ):

            answer = get_ai_response(
                prompt
            )

        with st.spinner(
            "Generating voice response..."
        ):

            audio_reply = text_to_speech(
                answer
            )

        with st.chat_message(
            "assistant"
        ):

            st.markdown(
                answer
            )

            st.audio(
                audio_reply,
                format="audio/mp3"
            )

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

    st.markdown("---")

    txt_content = ""

    for msg in st.session_state.messages:

        txt_content += (
            f"{msg['role'].upper()}: "
            f"{msg['content']}\n\n"
        )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="⬇ Download TXT",
            data=txt_content,
            file_name="chat_history.txt",
            mime="text/plain"
        )

    with col2:

        pdf_file = create_chat_pdf(
            st.session_state.messages
        )

        st.download_button(
            label="⬇ Download PDF",
            data=pdf_file,
            file_name="chat_history.pdf",
            mime="application/pdf"
        )