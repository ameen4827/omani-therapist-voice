# 🧠 Sakeenah: Omani Therapist Voice Assistant

**Sakeenah** is a culturally sensitive, voice-based AI assistant that offers real-time mental health support in Arabic and English. It integrates Islamic coping strategies, cognitive behavioral therapy (CBT) insights, and modern LLMs (like GPT-4o and Claude Opus 4) using the **Model-Context Protocol (MCP)** to guide interactions.


---

🔑 OpenRouter Integration

Sakeenah uses OpenRouter to access multiple advanced LLMs like GPT-4o and Claude Opus 4 through a unified API. This enables a robust fallback mechanism—if one model fails or is slow, another responds seamlessly. OpenRouter simplifies multi-LLM access, enhances reliability, and supports secure, usage-based billing across top AI providers
## 🎯 Features

- 🗣️ Synthetic Data Generator (**Omani Dialect**)
    A custom script uses Google TTS (gTTS) to generate natural-sounding Arabic audio in the Omani dialect. It covers all key mental health scenarios (e.g., crisis, stress, family issues) to simulate real user      input for testing the full voice pipeline. This ensures consistent evaluation without needing live recordings.
- 🎤 Real-time **voice input** or uploaded `.wav` files   
- 🧠 **Crisis detection** (e.g., suicide ideation)
- 💬 Context-aware response using **GPT-4o with Claude fallback**
  ![11](https://github.com/user-attachments/assets/10ceedf8-99d7-4227-81c6-d4123e2cca82)

- 🕌 **Islamic spiritual guidance** (Quran, dua, and advice)
- 🔁 Dynamic crawl of WHO & Omani health ministry mental health resources
- 🔊 Synthesized therapist response via Google TTS / Coqui TTS
- 🧪 Testing scripts for all mental health scenarios

---
⚡ Latency Performance

Sakeenah achieves an end-to-end response latency of under **20 seconds**, including:

🎙️ Audio input (recording/upload)

🧠 Whisper transcription (STT)

🧩 Context detection & LLM response (GPT-4o / Claude)

🔊 Voice synthesis (TTS)

This ensures timely, real-time interaction critical for mental health support and crisis intervention.



## 🛠️ Installation & Setup
```bash
1️) Clone Repository
git clone https://github.com/ameen4827/omani-therapist-voice.git
cd omani-therapist-voice

2) Create Conda Environment

conda create -n omani-therapist-voice python=3.10 -y
conda activate omani-therapist-voice

3) Install Dependencies
pip install -r requirements.txt

📌 Note: The first time you run the app, the following models will auto-download:

Model	-> Purpose	-> Download Location
Whisper (base) ->	Speech-to-text ->	~/.cache/whisper

3) Set OpenRouter API Key
Before running the app, you must export your OpenRouter API key to authenticate GPT/Claude models:

export OPENROUTER_API_KEY= <OPENROUTER_API_KEY>

export OPENROUTER_API_KEY="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"

4) Run the App
streamlit run app.py

5) Input Options
   - 🎧 Record using your microphone

   - 📁 Upload an existing .wav file

   - 🏷️ Automatically detects:

        Crisis: "أفكر أن أنهي حياتي"
        
        Stress: "الدوام متعب"
        
        Anger: "أنا عصبي"
        
        Sleep: "ما أقدر أنام"
        
        Code-switch: "I'm tired من كل شيء"
6) Testing
   ### 🧪 Test Cases https://github.com/ameen4827/omani-therapist-voice/tree/main/tests/cases
   Run:
    1. To check context adapter 

       python test_context_adapter.py

     🧪 Context Adapter Test Results

      ---
      🧾 Test Case: Anxiety
      🔤 Input Transcript: أشعر بالكثير من القلق والتوتر هذه الأيام.
      🧠 Adapted Transcript: المستخدم يعاني من القلق أو التوتر. شجعه على التنفس العميق والتعامل مع مصادر القلق. أشعر بالكثير من القلق والتوتر هذه الأيام.
      🏷️ Detected Label: general_anxiety

      2. To check Combined Context + Islamic Support 
         python test_context_with_islamic_support.py

     🧪 Combined Context + Islamic Support Test Results

        ---
        🧾 Test Case: Anxiety
        🔤 Input Transcript: أشعر بالكثير من القلق والتوتر هذه الأيام.
        🧠 Adapted Transcript: المستخدم يعاني من القلق أو التوتر. شجعه على التنفس العميق والتعامل مع مصادر القلق. أشعر بالكثير من القلق والتوتر هذه الأيام.
        🏷️ Detected Label: general_anxiety
        🕌 Islamic Topic: القلق والتوتر
        📖 Quran:
          → ﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ - الرعد: 28
        🤲 Dua:- اللهم إني أعوذ بك من الهم والحزن، والعجز والكسل...
        📘 Advice: القلق من الابتلاءات أمر طبيعي. تذكر أن الله مع الصابرين، وأن كل ضيق يعقبه فرج.
        
        ---
        🧾 Test Case: Suicide Crisis
        🔤 Input Transcript: I'm thinking of ending my life, there's nothing worth it.
        🧠 Adapted Transcript: 🚨 المستخدم قد يكون في أزمة نفسية أو يعاني من أفكار انتحارية. الرجاء الرد بتعاطف وهدوء، وتجنب أي أحكام. شجعه على طلب المساعدة من مختص. I'm thinking of ending my life, there's nothing worth it.
        🏷️ Detected Label: crisis_suicide
        🕌 Islamic Topic: أزمة نفسية أو انتحار
        📖 Quran:
          → ﴿وَلَا تَقْتُلُوا أَنفُسَكُمْ﴾ - النساء: 29
          → ﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾ - الشرح: 6
        🤲 Dua:
          - اللهم ارح قلبي مما يؤلمني، وامنحني القوة والصبر.
        📘 Advice: الله أرحم بك من نفسك. اطلب المساعدة، فالانتحار ليس حلاً، بل صبرك أجره عظيم.
        
        ---
        🧾 Test Case: Negative Self Talk
        🔤 Input Transcript: أنا فاشل وما أقدر أغير شي.
        🧠 Adapted Transcript: المستخدم يعاني من أفكار سلبية عن نفسه. استجب بأسلوب تعاطفي وأعد توجيه تفكيره نحو الإيجابية. أنا فاشل وما أقدر أغير شي.
        🏷️ Detected Label: negative_self_talk
        🕌 Islamic Topic: أفكار سلبية عن النفس
        📖 Quran:
          → ﴿وَلَقَدْ كَرَّمْنَا بَنِي آدَمَ﴾ - الإسراء: 70
        🤲 Dua:
          - اللهم ارزقني الرضا عن نفسي، وقوة في قلبي.
        📘 Advice: أنت مكرم عند الله. لا تحكم على نفسك بقسوة، واستبدل الحديث السلبي بالتفاؤل.



    3. To generate synthetic audio:
       python generate_keyword_test_wavs.py

🌐 External Integration
✅ OpenRouter API (GPT-4o, Claude 3.5)

✅ WHO EMRO & MOH Oman crawling

✅ MCP-based interaction pipeline

✅ Islamic mental health adapter






   


