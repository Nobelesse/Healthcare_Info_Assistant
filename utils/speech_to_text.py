import speech_recognition as sr
import tempfile
from pydub import AudioSegment


def transcribe_audio(audio_bytes):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio_bytes)

            temp_audio_path = temp_audio.name

        recognizer = sr.Recognizer()

        with sr.AudioFile(
            temp_audio_path
        ) as source:

            audio_data = recognizer.record(
                source
            )

        text = recognizer.recognize_google(
            audio_data
        )

        return text

    except Exception as e:

        return f"Speech Recognition Error: {e}"