# test_context_adapter.py

from context_adapter import adapt_transcript_context

# Sample test inputs
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

# File to save the test results
output_file = "context_test_results.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("🧪 Context Adapter Test Results\n\n")
    
    for case, transcript in test_inputs.items():
        adapted, label = adapt_transcript_context(transcript)
        result = (
            f"---\n"
            f"🧾 Test Case: {case}\n"
            f"🔤 Input Transcript: {transcript}\n"
            f"🧠 Adapted Transcript: {adapted}\n"
            f"🏷️ Detected Label: {label}\n\n"
        )
        print(result)  # Optional: comment this if you only want file output
        f.write(result)

print(f"✅ All results written to: {output_file}")
