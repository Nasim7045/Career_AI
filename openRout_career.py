
import requests

OPENROUTER_API_KEY = ""  # Get from https://openrouter.ai/keys
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

conversation_history = []

print("🎓 Welcome to the AI Career Guidance Assistant (Powered by OpenRouter)!")
print("Ask any question related to your career or education path.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("🧑 You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("👋 Thank you for using the AI Career Guidance Assistant. Good luck!")
        break

    conversation_history.append({"role": "user", "content": user_input})

    try:
        payload = {
            "model": "deepseek/deepseek-chat",  # Free model
            "messages": conversation_history,
            "temperature": 0.7,
            "max_tokens": 1000
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        response_data = response.json()

        if response.status_code == 200:
            ai_reply = response_data["choices"][0]["message"]["content"]
            print("\n🤖 AI Assistant:", ai_reply.strip(), "\n")
            conversation_history.append({"role": "assistant", "content": ai_reply})
        else:
            print("❌ Error:", response_data.get('error', 'Unknown error'), "\n")

    except Exception as e:
        print("❌ An error occurred:", str(e), "\n")
