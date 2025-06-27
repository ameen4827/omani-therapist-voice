# app.py

import streamlit as st
import sounddevice as sd
import numpy as np
import whisper
import tempfile
import os
import time
from scipy.io.wavfile import write
from openai import OpenAI
import tiktoken

# Local modules
#from tts_coqui import synthesize_arabic_coqui
from tts_google import synthesize_google_tts
from context_adapter import adapt_transcript_context
from islamic_adapter import get_islamic_support
from static_mental_health_links import mental_health_resources

# ✅ OpenRouter key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    st.error("❌ Please set OPENROUTER_API_KEY in your environment.")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

# ✅ Load Whisper
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("tiny")

whisper_model = load_whisper_model()

# ✅ Audio handling
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

def count_tokens(text, model="gpt-4o"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def estimate_cost(input_tokens, output_tokens):
    return (input_tokens / 1000) * 0.005 + (output_tokens / 1000) * 0.015

def chat_with_models(transcript, max_out_tokens=500):
    system_prompt = (
        "You are a culturally sensitive Omani Arabic-speaking therapist. "
        "Respect Islamic cultural norms and respond."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": transcript}
    ]

    start = time.time()
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=max_out_tokens
        )
        reply = response.choices[0].message.content
        latency = round(time.time() - start, 2)
        model_used = "GPT-4o"
    except Exception as e:
        st.warning(f"⚠️ GPT-4o failed: {str(e)}. Switching to Claude 3.5 Sonnet...")
        fallback_start = time.time()
        response = client.chat.completions.create(
            model="anthropic/claude-3.5-sonnet",
            messages=messages,
            temperature=0.7,
            max_tokens=max_out_tokens
        )
        reply = response.choices[0].message.content
        latency = round(time.time() - fallback_start, 2)
        model_used = "Claude 3.5"

    in_tok = count_tokens(system_prompt + transcript)
    out_tok = count_tokens(reply)
    cost = estimate_cost(in_tok, out_tok)

    return reply, latency, in_tok, out_tok, cost, model_used

# ✅ UI Layout
st.set_page_config(page_title="🧠 Sakeenah: صوتك... وعونك وقت الحاجة. - OMANI-Therapist-Voice" , layout="wide")
st.title("🧠 Sakeenah: صوتك... وعونك وقت الحاجة.- OMANI-Therapist-Voice")
st.caption("🎙️ تحدث بالعربية للحصول على دعم نفسي وثقافي حقيقي.")

col1, col2 = st.columns([3, 2])
context_label = None

with col1:
    st.markdown("### 🎧 Input Method")
    input_method = st.radio("Choose how to provide audio:", ["🎙️ Record", "📁 Upload"], horizontal=True)

    duration = st.slider("⏱️ Recording duration (sec)", 3, 10, 5)
    #tts_choice = st.radio("🔊 Choose TTS Engine", ["Coqui (Local)", "Google TTS"], horizontal=True)
    tts_choice = st.radio("🔊 Choose TTS Engine", [ "Google TTS"], horizontal=True)

    audio_path = None
    rate = 16000  # default

    if input_method == "🎙️ Record":
        if st.button("⏺️ Record Now"):
            audio, rate = record_audio(duration)
            audio_path = save_temp_wav(audio, rate)

    elif input_method == "📁 Upload":
        uploaded_file = st.file_uploader("📁 Upload WAV file", type=["wav"])
        if uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(uploaded_file.read())
                audio_path = tmp.name
                st.success("✅ Audio uploaded successfully!")

    # Proceed if audio path exists
    if audio_path:
        with st.spinner("🔤 Transcribing..."):
            stt_start = time.time()
            transcript = transcribe(audio_path)
            stt_latency = round(time.time() - stt_start, 2)

        st.audio(audio_path, format="audio/wav")
        st.markdown(f"**📝 Transcript:** `{transcript}`")
        st.markdown(f"🕐 STT Latency: `{stt_latency}s`")

        with st.spinner("🧠 Adapting context..."):
            adapted_transcript, context_label = adapt_transcript_context(transcript)
            st.markdown(f"🧠 **Context Detected:** `{context_label}`")
            st.markdown(f"🔄 Adapted Transcript: {adapted_transcript}")

        with st.spinner("💬 Generating Therapist Response..."):
            reply, gpt_latency, in_tok, out_tok, cost, model_used = chat_with_models(adapted_transcript)

        st.success(f"🤖 **Therapist ({model_used}):** {reply}")
       

        st.markdown("📊 **Session Stats**")
        st.markdown(f"⚡ GPT Latency: `{gpt_latency}s` | STT: `{stt_latency}s` | Total: `{gpt_latency + stt_latency}s`")
        st.markdown(f"🧮 Tokens - In: `{in_tok}`, Out: `{out_tok}`, Total: `{in_tok + out_tok}`")
        st.markdown(f"💰 Est. Cost: `${cost:.4f}`")
        with st.spinner("🔊 Synthesizing Voice..."):
            if tts_choice == "Coqui (Local)":
                #wav_path = synthesize_arabic_coqui(reply)
                #st.audio(wav_path, format="audio/wav")
                pass
            else:
                mp3_path = synthesize_google_tts(reply)
                st.audio(mp3_path, format="audio/mp3")
       

with col2:
    st.subheader("🕌 Islamic Support")
    
    if context_label:
        islamic_data = get_islamic_support(context_label)

        if islamic_data:
            st.markdown(f"#### 🏷️ **الموضوع:** {islamic_data['topic']}")

            st.markdown("#### 📖 **آيات من القرآن:**")
            for ayah in islamic_data.get("quran", []):
                st.markdown(f"- {ayah}")

            if islamic_data.get("dua"):
                st.markdown("#### 🤲 **دعاء مقترح:**")
                st.markdown(f"> *{islamic_data['dua'][0]}*")

            if islamic_data.get("advice"):
                st.markdown("#### 🧠 **نصيحة إيمانية:**")
                st.markdown(f"> *{islamic_data['advice']}*")

        else:
            st.info("❌ لا يوجد دعم إسلامي محدد لهذا السياق.")
    else:
        st.info("⏳ بانتظار إدخال المستخدم...")

    st.subheader("🌐 Mental Health Resources")
    if context_label:
        resources = mental_health_resources.get(context_label, [])
        if resources:
            for item in resources:
                st.markdown(f"- [{item['text']}]({item['url']})")
        else:
            st.info("🚫 لا توجد روابط محددة لهذا السياق.")
