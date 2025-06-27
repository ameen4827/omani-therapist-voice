# tts_coqui.py

from TTS.api import TTS
from scipy.io.wavfile import write
import tempfile
import os

# ✅ Use a multilingual Arabic-capable model
MODEL_NAME = "tts_models/multilingual/multi-dataset/your_tts"

# Initialize only once
tts = TTS(model_name=MODEL_NAME, progress_bar=False, gpu=False)

def synthesize_arabic_coqui(text):
    """
    Synthesizes Arabic speech using Coqui TTS (offline).
    Returns path to generated .wav file.
    """
    waveform = tts.tts(text)
    sample_rate = tts.synthesizer.output_sample_rate

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        write(f.name, sample_rate, waveform)
        return f.name
