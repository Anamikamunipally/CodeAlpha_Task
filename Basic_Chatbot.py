def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["hello", "hi"]:
            print("Chatbot: Hi there!")
        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks!")
        elif user_input in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! 👋")
            break
        else:
            print("Chatbot: Sorry, I don’t understand that.")

if __name__ == "__main__":
    chatbot()
