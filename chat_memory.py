from model_loader import chat_pipeline
conversation = ""

def chatbot(user_input):
    global conversation
    conversation +=(f"\nUser:{user_input}\nBot:")
    output = chat_pipeline(conversation)[0]["generated_text"]
    
    if "Bot:" in output:
     answer = output.split("Bot:")[-1].strip()
     answer = answer.split(".")[0]
     conversation += " " + answer
    return answer
print("success")