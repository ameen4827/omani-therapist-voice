# generate_keyword_test_wavs.py

from gtts import gTTS
from pydub import AudioSegment
import os

OUTPUT_DIR = "keyword_test_wavs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 🧠 Test sentences covering each keyword category
test_cases = {
    # Crisis
    "crisis_suicide_1": "أفكر في الانتحار. ما في فائدة.",
    "crisis_suicide_2": "I want to end my life. everything feels dark.",

    # Negative Self Talk
    "negative_self_talk_1": "أنا فاشل، ما أقدر أسوي شيء.",
    "negative_self_talk_2": "I'm a failure and hopeless.",

    # Catastrophic Thinking
    "catastrophic_thinking_1": "كل شيء خرب، ما راح يتحسن الوضع.",
    "catastrophic_thinking_2": "It’s hopeless. Everything is ruined.",

    # Avoidance / Withdrawal
    "avoidance_withdrawal_1": "ما أحب أتكلم مع أي أحد.",
    "avoidance_withdrawal_2": "I just stay in bed all day. I isolate.",

    # General Anxiety
    "general_anxiety_1": "أشعر بقلق شديد وتوتر.",
    "general_anxiety_2": "I'm tired and feel disconnected lately.",

    # Sleep Issues
    "sleep_disorder_1": "ما قدرت أنام أمس، عندي أرق.",
    "sleep_disorder_2": "I can't sleep at night, insomnia is killing me.",

    #Work Stress
    "work_stress_1": "الضغط في الشغل زايد عن حده.",
    "work_stress_2": "Too many deadlines and I feel overwhelmed.",

    # 🧠 Trauma
    "trauma_1": "أحلم بكوابيس دايمًا، وأتذكر العنف.",
    "trauma_2": "I was abused and still have nightmares.",

    # 🧠 Family Stress
    "family_stress_1": "أمي دايمًا تقارنني بأختي.",
    "family_stress_2": "My parents put too much pressure on me.",

    # 🧠 Anger
    "anger_1": "أنا عصبي جدًا lately.",
    "anger_2": "I'm angry and frustrated all the time.",
}


def generate_wav(text, label):
    mp3_path = os.path.join(OUTPUT_DIR, f"{label}.mp3")
    wav_path = os.path.join(OUTPUT_DIR, f"{label}.wav")

    try:
        # Create TTS (Arabic or mixed)
        tts = gTTS(text=text, lang="ar" if all(ord(c) < 128 for c in text) is False else "en")
        tts.save(mp3_path)

        # Convert to WAV
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")

        print(f"[✅] {label}.wav saved.")
    except Exception as e:
        print(f"[❌] Failed to generate {label}: {e}")


if __name__ == "__main__":
    for label, text in test_cases.items():
        generate_wav(text, label)
