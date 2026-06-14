import streamlit as st

from streamlit_mic_recorder import (
    mic_recorder
)

st.title("🎤 Voice Notes")

audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    just_once=True
)

if audio:

    st.success(
        "Recording Captured"
    )

    st.audio(
        audio["bytes"]
    )