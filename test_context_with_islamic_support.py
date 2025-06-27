# test_context_with_islamic_support.py

from context_adapter import adapt_transcript_context
from islamic_adapter import get_islamic_support

# 📋 Test Cases
test_inputs = {
    "Anxiety": "أشعر بالكثير من القلق والتوتر هذه الأيام.",
    "Suicide Crisis": "I'm thinking of ending my life, there's nothing worth it.",
    "Negative Self Talk": "أنا فاشل وما أقدر أغير شي.",
    "Catastrophic Thinking": "كل شيء خرب، الوضع ميؤوس منه.",
    "Avoidance": "ما أحب أتكلم مع أحد، وأفضل أبقى في غرفتي.",
    "Depression": "ما في أمل، الاكتئاب خانقني.",
    "Work Stress": "الدوام يضغطني نفسيًا، والمدير ما يرحم.",
    "Sleep Issues": "ما أقدر أنام، عندي أرق مستمر.",
    "Anger": "أغضب بسرعة وما أتحكم في أعصابي.",
    "Family Conflict": "أنا وأمي نتشاجر دائمًا، ما في تفاهم.",
    "Trauma": "violence أحلم بكوابيس بسبب العنف اللي شفته."
}

# 📝 Output file
output_file = "context_islamic_test_results.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("🧪 Combined Context + Islamic Support Test Results\n\n")

    for case, transcript in test_inputs.items():
        adapted, label = adapt_transcript_context(transcript)
        support = get_islamic_support(label)

        # ✅ Print section
        f.write(f"---\n🧾 Test Case: {case}\n")
        f.write(f"🔤 Input Transcript: {transcript}\n")
        f.write(f"🧠 Adapted Transcript: {adapted}\n")
        f.write(f"🏷️ Detected Label: {label}\n")

        if support:
            f.write(f"🕌 Islamic Topic: {support['topic']}\n")
            f.write("📖 Quran:\n")
            for verse in support["quran"]:
                f.write(f"  → {verse}\n")
            f.write("🤲 Dua:\n")
            for d in support["dua"]:
                f.write(f"  - {d}\n")
            f.write(f"📘 Advice: {support['advice']}\n")
        else:
            f.write("🕌 No Islamic support found for this label.\n")

        f.write("\n")

print(f"✅ Test completed. Results saved to: {output_file}")
