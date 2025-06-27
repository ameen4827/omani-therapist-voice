# 🧠 Sakeenah: Omani Therapist Voice Assistant

**Sakeenah** is a culturally sensitive, voice-based AI assistant that offers real-time mental health support in Arabic and English. It integrates Islamic coping strategies, cognitive behavioral therapy (CBT) insights, and modern LLMs (like GPT-4o and Claude 3.5) using the **Model-Context Protocol (MCP)** to guide interactions.

---

## 🎯 Features

- 🎤 Real-time **voice input** or uploaded `.wav` files
- 🧠 **Crisis detection** (e.g., suicide ideation)
- 💬 Context-aware response using **GPT-4o with Claude fallback**
- 🕌 **Islamic spiritual guidance** (Quran, dua, and advice)
- 🔁 Dynamic crawl of WHO & Omani health ministry mental health resources
- 🔊 Synthesized therapist response via Google TTS / Coqui TTS
- 🧪 Testing scripts for all mental health scenarios

---

## 🛠️ Installation & Setup

1️) Clone Repository

```bash
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
        🤲 Dua:
          - اللهم إني أعوذ بك من الهم والحزن، والعجز والكسل...
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


🙏 Acknowledgments
    OpenRouter.ai
    
    Whisper by OpenAI
    
    Coqui TTS
    
    WHO EMRO

🧠 License
   For academic, research, and non-commercial use only.

🤝 Contributors
   Made with ❤️ for mental well-being by Ameen
