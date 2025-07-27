from emotion_detector import detect_emotion
from chatbot_response import chat_with_gpt, reset_chat

# Optional: Uncomment for color output (install with `pip install colorama`)
# from colorama import init, Fore, Style
# init(autoreset=True)

def main():
    print("=" * 50)
    print("🧠 Emotion-Aware Chatbot")
    print("Type 'reset' to clear chat or 'exit' to quit.")
    print("=" * 50)

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("⚠️ Please enter something.")
            continue

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        if user_input.lower() == "reset":
            reset_chat()
            print("🔄 Chat history reset.")
            continue

        try:
            # Detect emotion
            emotion, confidence = detect_emotion(user_input)
            print(f"[Detected Emotion: {emotion.upper()} ({confidence * 100:.1f}%)]")

            # Generate chatbot reply
            reply = chat_with_gpt(user_input, emotion=emotion)
            print("Bot:", reply)

        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
