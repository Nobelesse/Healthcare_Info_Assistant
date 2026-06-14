import speech_recognition as sr
import tempfile
from pydub import AudioSegment
import os


def transcribe_audio(audio_bytes):

    try:

        # Save microphone recording as WebM
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".webm"
        ) as temp_webm:

            temp_webm.write(audio_bytes)
            webm_path = temp_webm.name

        # Create WAV output file
        wav_path = webm_path.replace(
            ".webm",
            ".wav"
        )

        # Convert WebM -> WAV
        audio = AudioSegment.from_file(
            webm_path,
            format="webm"
        )

        audio.export(
            wav_path,
            format="wav"
        )

        recognizer = sr.Recognizer()

        with sr.AudioFile(wav_path) as source:

            audio_data = recognizer.record(
                source
            )

        text = recognizer.recognize_google(
            audio_data
        )

        os.remove(webm_path)
        os.remove(wav_path)

        return text

    except Exception as e:

        return f"Speech Recognition Error: {e}"