# test_google_tts.py

from gtts import gTTS
from pydub import AudioSegment
import os
from datetime import datetime

OUTPUT_DIR = "tts_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def synthesize_google_tts(text="i want to end my life", lang="ar"):
    """
    Synthesizes Arabic speech using Google TTS and saves a .wav file
    to the tts_outputs/ folder with a timestamped filename.
    Returns the full path to the WAV file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    mp3_path = os.path.join(OUTPUT_DIR, f"gtts_{timestamp}.mp3")
    wav_path = os.path.join(OUTPUT_DIR, f"gtts_{timestamp}.wav")

    # Generate and save MP3
    gTTS(text=text, lang=lang).save(mp3_path)

    # Convert to WAV
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

    return wav_path


if __name__ == "__main__":
    synthesize_google_tts()
