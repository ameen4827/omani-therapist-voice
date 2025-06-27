# generate_test_wavs.py

from gtts import gTTS
from pydub import AudioSegment
import os
from datetime import datetime

# Output folder
OUTPUT_DIR = "generated_wavs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Test cases: (label, transcript)
test_cases = [
    ("general_anxiety", "أحس بقلق دائم، حتى لما أكون مرتاح. قلبي يدق بسرعة وأفكاري مشوشة."),
    ("family_stress", "أشعر أن أمي ما تفهمني، دايمًا تقول لي لازم أكون مثل أخوي الكبير. هذا يضغطني كثير."),
    ("work_stress", "الدوام صاير مرهق جدًا، كل يوم اجتماعات وتقارير، ما ألحق أرتاح. أحس نفسي مضغوط طول الوقت."),
    ("crisis_suicide", "أفكر كثير في إنهاء حياتي، ما أحس أن في أحد يفهمني. كل شيء غامق وما في أمل."),
    ("code_switching", "أنا so tired lately. I just feel disconnected من كل شيء. ما عندي طاقة أكمل."),
]

def synthesize_wav(text, label, lang="ar"):
    # Save MP3
    mp3_path = os.path.join(OUTPUT_DIR, f"{label}.mp3")
    wav_path = os.path.join(OUTPUT_DIR, f"{label}.wav")

    tts = gTTS(text=text, lang=lang)
    tts.save(mp3_path)

    # Convert to WAV
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    print(f"[✅] Saved: {wav_path}")

if __name__ == "__main__":
    for label, text in test_cases:
        synthesize_wav(text, label)
