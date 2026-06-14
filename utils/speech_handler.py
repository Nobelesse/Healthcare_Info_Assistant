import tempfile

from gtts import gTTS
from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
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
    segments, info = model.transcribe(audio_path)

    text = " ".join(
        segment.text
        for segment in segments
    )

    return text.strip()


def text_to_speech(text):
    tts = gTTS(
        text=text,
        lang="en"
    )

    temp_mp3 = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    temp_mp3.close()

    tts.save(temp_mp3.name)

    return temp_mp3.name