import streamlit as st
import sounddevice as sd
import numpy as np
import whisper
import tempfile
import os
import time
from scipy.io.wavfile import write

from context_adapter import adapt_transcript_context
from llm_client import chat_with_models
from static_mental_health_links import mental_health_resources
# ✅ Set API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    st.error("❌ Please set OPENROUTER_API_KEY in your environment.")
    st.stop()

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

whisper_model = load_whisper_model()

def record_audio(duration=5, fs=16000):
    st.info(f"🎤 Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return np.squeeze(audio), fs

def save_temp_wav(audio_data, sample_rate):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        write(tmpfile.name, sample_rate, (audio_data * 32767).astype(np.int16))
        return tmpfile.name

def transcribe(audio_path):
    result = whisper_model.transcribe(audio_path, language="ar", fp16=False)
    return result["text"]

st.set_page_config(page_title="🧠 Omani Therapist Voice", layout="centered")
st.title("🧠 Omani Therapist (MCP Version)")
st.caption("🎙️ Speak Arabic to get real-time culturally sensitive support.")

duration = st.slider("🎙️ Recording duration (sec)", 3, 10, 5)

if st.button("🎧 Record & Respond"):
    audio, rate = record_audio(duration)
    audio_path = save_temp_wav(audio, rate)

    with st.spinner("⏱️ Transcribing..."):
        transcript = transcribe(audio_path)

    st.audio(audio_path, format="audio/wav")
    st.markdown(f"**📝 Transcript:** `{transcript}`")
    

    # 🔄 MCP Adapter for contextual prompt modification
    adapted_transcript = adapt_transcript_context(transcript)
    if "🚨" in adapted_transcript:
        st.error("🚨 هذه حالة أزمة محتملة. يرجى التواصل مع جهة مختصة فورًا.")
        st.markdown("""
        ### 📞 جهات اتصال الطوارئ النفسية في سلطنة عُمان:
        - **مستشفى ابن سينا للصحة النفسية** – الخط الساخن: `+968-24xxxxxx`
        - **مركز الدعم الوطني للصحة النفسية** – `247xxxxx`
        - **مركز شفاء للاستشارات النفسية** – `+968-9xxxxxxx`
        - أو راجع أقرب مركز صحي فورًا.
        """)

   

    messages = [
        {"role": "system", "content": "You are a culturally sensitive Omani therapist."},
        {"role": "user", "content": adapted_transcript}
    ]

    st.header("🌐 مصادر دعم الصحة النفسية")

    for category, links in mental_health_resources.items():
        readable = category.replace("_", " ").title()
        st.subheader(f"🔖 {readable}")
        for item in links:
            st.markdown(f"- [{item['text']}]({item['url']})")

    #with st.spinner("🧠 Generating Therapist Reply..."):
    #    reply, latency, model_used = chat_with_models(messages)

    
    #st.success(f"🤖 **Therapist ({model_used}):** {reply}")
    #st.markdown(f"⚡ Latency: `{latency}s`")