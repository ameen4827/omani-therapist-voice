# test_coqui_tts.py

from TTS.api import TTS
from scipy.io.wavfile import write
import tempfile
import os

# ✅ Use a multilingual Arabic-supported model
MODEL_NAME = "tts_models/multilingual/multi-dataset/your_tts"

def synthesize_arabic_coqui(text="أنا هنا لمساعدتك. تذكر أنك لست وحدك."):
    try:
        tts = TTS(model_name=MODEL_NAME, progress_bar=False, gpu=False)
        waveform = tts.tts(text)
        sample_rate = tts.synthesizer.output_sample_rate

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            write(f.name, sample_rate, waveform)
            print(f"[✅] Coqui TTS: Audio saved to {f.name}")
            return f.name
    except Exception as e:
        print(f"[❌] Coqui TTS Error: {e}")

if __name__ == "__main__":
    synthesize_arabic_coqui()
