def adapt_transcript_context(user_transcript):
    """
    Adds culturally sensitive context, CBT techniques, and suicide risk escalation.
    Handles Arabic-English mental health vocabulary and code-switching.
    """

    lowered = user_transcript.lower()
    print(lowered)

    # 🚨 Suicide/Crisis Detection
    crisis_keywords = [
        "أريد أن أنهي حياتي", "أفكر في الانتحار", "ما في فائدة أعيش", "أريد أن أرتاح إلى الأبد",
        "I want to die", "I want to end it all", "suicide", "kill myself",
        "no reason to live", "cut myself", "self-harm", "hurt myself", "ending my life",
        "ما أقدر أتحمل", "أكره حياتي", "ما في شيء يستاهل"
    ]

    if any(kw in user_transcript or kw in lowered for kw in crisis_keywords):
        return (
            "🚨 المستخدم قد يكون في خطر انتحار أو أزمة نفسية حادة. "
            "استجب بتعاطف، لا تقدم نصائح طبية، وشجعه على طلب مساعدة فورية من مختص أو جهة طوارئ. "
            "إذا كنت تراه بحاجة، اقترح عليه الاتصال بالخط الساخن للصحة النفسية. "
            f"{user_transcript}"
        )

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

    # 🧠 General Symptoms
    anxiety_keywords = ["قلق", "توتر", "anxiety", "panic", "nervous"]
    depression_keywords = ["اكتئاب", "حزين", "depression", "hopeless"]
    stress_keywords = ["ضغط", "إرهاق", "stress", "overwhelmed"]
    sleep_keywords = ["أرق", "نوم", "insomnia", "can't sleep"]
    trauma_keywords = ["صدمة", "كابوس", "trauma", "nightmare", "abuse"]
    anger_keywords = ["غضب", "عصبية", "angry", "frustrated"]

    # Inject CBT-informed prompts
    if any(p in user_transcript or p in lowered for p in negative_self_talk):
        return "المستخدم لديه أفكار سلبية عن الذات. ساعده بإعادة هيكلة هذه الأفكار باستخدام أساليب العلاج المعرفي السلوكي (CBT). " + user_transcript
    elif any(p in user_transcript or p in lowered for p in catastrophic_thinking):
        return "المستخدم يُظهر تفكيرًا كارثيًا. شجعه على تقييم هذه التوقعات باستخدام الأسئلة السقراطية. " + user_transcript
    elif any(p in user_transcript or p in lowered for p in avoidance_or_withdrawal):
        return "المستخدم يميل إلى الانسحاب أو التجنب. اقترح عليه خطوات صغيرة نحو التفعيل السلوكي (Behavioral Activation). " + user_transcript
    elif any(p in user_transcript or p in lowered for p in anxiety_keywords):
        return "المستخدم يعاني من القلق. استخدم CBT لتحديد الأفكار المثيرة للقلق وإعادة هيكلتها. " + user_transcript
    elif any(p in user_transcript or p in lowered for p in depression_keywords):
        return "المستخدم يظهر عليه أعراض الاكتئاب. حاول مساعدته على إيجاد أنشطة إيجابية أو أفكار بديلة. " + user_transcript
    elif any(p in user_transcript or p in lowered for p in stress_keywords):
        return "المستخدم يشعر بالإرهاق أو الضغط النفسي. اقترح عليه تقنيات الاسترخاء والتنظيم العاطفي. " + user_transcript
    elif any(p in user_transcript or p in lowered for p in sleep_keywords):
        return "المستخدم يواجه مشكلات في النوم. اقترح عليه عادات نوم صحية أو تمارين استرخاء. " + user_transcript,"general_anxiety"
    elif any(p in user_transcript or p in lowered for p in trauma_keywords):
        return "المستخدم يشير إلى تجربة صادمة. كن داعمًا ووجهه نحو المساعدة المتخصصة دون التحقيق أو الضغط. " + user_transcript
    elif any(p in user_transcript or p in lowered for p in anger_keywords):
        return "المستخدم يعبر عن الغضب أو الإحباط. ساعده على فهم مشاعره واقتراح تقنيات لتنظيمها. " + user_transcript,"general_anxiety"

    return user_transcript
