from openai import OpenAI
import os
import time

# ✅ Set OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)
def chat_with_models(messages, max_out_tokens=100):
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
    except Exception:
        response = client.chat.completions.create(
            model="anthropic/claude-3.5-sonnet",
            messages=messages,
            temperature=0.7,
            max_tokens=max_out_tokens
        )
        reply = response.choices[0].message.content
        latency = round(time.time() - start, 2)
        model_used = "Claude 3.5"
    return reply, latency, model_used