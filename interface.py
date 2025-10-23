from chat_memory import chatbot

while True:
    user_input = input("User: ")
    if user_input.lower() == "/exit":
        print("Exiting chatbot. Goodbye!")
        break
    bot_response = chatbot(user_input)
    print(f"Bot:{bot_response}\n")

