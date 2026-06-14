import tempfile

from openai import OpenAI
from gtts import gTTS

import streamlit as st


client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


def save_audio(audio_bytes):

    temp_audio = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp_audio.write(audio_bytes)

    temp_audio.close()

    return temp_audio.name


def speech_to_text(audio_path):

    with open(audio_path, "rb") as audio_file:

        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    return transcript.text


def text_to_speech(text):

    tts = gTTS(
        text=text,
        lang="en"
    )

    temp_mp3 = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts.save(
        temp_mp3.name
    )

    return temp_mp3.name