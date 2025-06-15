import google.generativeai as genai

# ✅ Replace with your Gemini API key
API_KEY = ""

# Configure API
genai.configure(api_key=API_KEY)

# ✅ Efficient generation settings (customizable)
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

# ✅ Use low-cost, fast model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest", generation_config=generation_config)

# ✅ Start a chat session (for memory)
chat_session = model.start_chat(history=[])

print("🎓 Welcome to the AI Career Guidance Assistant!")
print("Ask any question related to your career or education path.")
print("Type 'exit' to quit.\n")

# Main loop
while True:
    user_input = input("🧑 You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("👋 Thank you for using the AI Career Guidance Assistant. Good luck!")
        break

    try:
        response = chat_session.send_message(user_input)
        print("\n🤖 AI Assistant:", response.text.strip(), "\n")
    except Exception as e:
        print("❌ An error occurred:", str(e), "\n")
