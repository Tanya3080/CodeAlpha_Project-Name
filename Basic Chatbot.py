def chatbot():
    print(" Chatbot: Hi! I am your simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print(" Chatbot: Hello! How can I help you?")
        elif "name" in user_input:
            print("Chatbot: My name is Chatpot.")
        elif "how are you" in user_input:
            print(" Chatbot: I am fine, thank you! What about you?")
        elif user_input in ["bye", "goodbye"]:
            print(" Chatbot: Goodbye! Have a nice day ")
            break
        else:
            print(" Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
