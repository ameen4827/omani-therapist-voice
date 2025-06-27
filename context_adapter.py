# context_adapter.py

def adapt_transcript_context(user_transcript):
    """
    Enhances user transcript with therapeutic context for the LLM.
    Also returns a context label (e.g., 'general_anxiety', 'crisis_suicide') for downstream use.
    """

    lowered = user_transcript.strip().lower()

    # 🚨 Crisis Detection
    crisis_keywords = [
        "أريد أن أنهي حياتي", "أفكر في الانتحار", "ما في فائدة", "suicide",
        "kill myself", "no reason to live",  "end my life","ending my life", "cut myself", "hurt myself"
    ]
    if any(kw in user_transcript or kw in lowered for kw in crisis_keywords):
        context = (
            "🚨 المستخدم قد يكون في أزمة نفسية أو يعاني من أفكار انتحارية. "
            "الرجاء الرد بتعاطف وهدوء، وتجنب أي أحكام. شجعه على طلب المساعدة من مختص. "
            + user_transcript
        )
        return context, "crisis_suicide"

    # 🧠 CBT Triggers
    negative_self_talk = [
        "أنا فاشل", "ما أقدر", "ما في فائدة", "I'm a failure", "I'm worthless", "hopeless"
    ]
    catastrophic_thinking = [
        "كل شيء خرب", "ما راح يتحسن", "Everything is ruined", "It’s hopeless"
    ]
    avoidance_or_withdrawal = [
        "ما أحب أتكلم", "ما أخرج", "I avoid everyone", "I stay in bed", "I isolate"
    ]

    if any(kw in user_transcript or kw in lowered for kw in negative_self_talk):
        return (
            "المستخدم يعاني من أفكار سلبية عن نفسه. استجب بأسلوب تعاطفي وأعد توجيه تفكيره نحو الإيجابية. " + user_transcript,
            "negative_self_talk"
        )
    if any(kw in user_transcript or kw in lowered for kw in catastrophic_thinking):
        return (
            "المستخدم يُظهر نمط تفكير كارثي. شجعه على إعادة التقييم الواقعي وتجزئة المشكلة. " + user_transcript,
            "catastrophic_thinking"
        )
    if any(kw in user_transcript or kw in lowered for kw in avoidance_or_withdrawal):
        return (
            "المستخدم يميل إلى الانسحاب أو التجنب. شجعه على اتخاذ خطوات صغيرة للتفاعل مع الآخرين. " + user_transcript,
            "avoidance_withdrawal"
        )

    # 🧠 General Symptoms
    symptom_map = {
        "general_anxiety": ["قلق", "توتر", "anxiety", "panic", "nervous","tired","feel disconnected"],
        "depression": ["اكتئاب", "حزين", "depression", "hopeless"],
        "work_stress": ["ضغط", "إرهاق", "stress", "overwhelmed"],
        "sleep_disorder": ["أرق", "نوم", "insomnia", "can't sleep"],
        "trauma": ["صدمة", "كابوس", "trauma", "nightmare","violence", "abuse"],
        "anger": ["غضب", "عصبية", "angry", "frustrated"],
        "family_stress": ["أمي", "أبي", "أختي", "أخوي", "عائلتي", "family", "parents", "زوجي", "زوجتي"]
    }

    context_templates = {
        "general_anxiety": "المستخدم يعاني من القلق أو التوتر. شجعه على التنفس العميق والتعامل مع مصادر القلق. ",
        "depression": "المستخدم يظهر عليه علامات الاكتئاب. حاول تقديم دعم إيجابي وسؤال عن الأمور التي تجلب له الراحة. ",
        "work_stress": "المستخدم يشتكي من ضغوط العمل. حاول تقديم طرق للتوازن بين الحياة والعمل وتخفيف الضغط. ",
        "sleep_disorder": "المستخدم يعاني من مشاكل في النوم. اقترح عليه روتينًا للنوم وممارسات استرخاء. ",
        "trauma": "المستخدم يشير إلى أعراض صدمة نفسية. استجب بحذر وتعاطف ووجهه لمختص إن أمكن. ",
        "anger": "المستخدم يعاني من نوبات غضب. اقترح عليه استراتيجيات تهدئة وطرق تعبير صحية. ",
        "family_stress": "المستخدم يواجه صعوبات في العلاقات العائلية. استجب بتفهم واقترح حلولًا قائمة على الحوار والصبر. "
    }

    for label, keywords in symptom_map.items():
        if any(kw in user_transcript or kw in lowered for kw in keywords):
            return context_templates[label] + user_transcript, label

    # ✅ Default fallback
    return user_transcript, None
