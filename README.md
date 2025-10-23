# Chatbot
This repository contains a full implementation of a memory-enabled conversational chatbot powered by a pre-trained Large Language Model (LLM) (Gemma 3-270m-it).  The core feature is the ability to maintain long-term dialogue coherence by managing and feeding the entire conversation history back to the model on every turn.

Features:
Context-aware responses (conversation memory)
Chat history maintained dynamically
Customizable model and tokenizer
Adjustable text-generation parameters (temperature, top-p, etc.)

🛠️ Requirements



Make sure you have the following installed:

python >= 3.8
transformers
torch
Optional: For running interactive chat or demos
sentencepiece>=0.2.0
accelerate>=0.33.0

📄 Project Structure
chatbot/
│
├── model_loader.py        # Loads the Hugging Face model and tokenizer
├── chat_memory.py         # Stores Conversation History of the Model
├── interface.py           # Chatbot Model inference
├── Demo Video             # code overview & inference of chatbot
└── README.md              # Project documentation

💡 How It Works

1.Load the model

from transformers import pipeline
chat_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=20,
    temperature=0.5,
    repetition_penalty=1.1
)


2.Chat function

from model_loader import chat_pipeline

conversation = ""

def chatbot(question):
    global conversation
    conversation += f"\nUser:{question}\nBot:"
    output = chat_pipeline(conversation)[0]["generated_text"]
    if "Bot:" in output:
        answer = output.split("Bot:")[-1].strip()
        conversation += " " + answer
    return answer


3.Run the chatbot

print(chatbot("What is AI?"))

To run from terminal:

python chatbot.py
You can modify the code to take user input continuously:
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", chatbot(user_input))

You: What is AI?
Bot: AI stands for Artificial Intelligence, a branch of computer science focused on building intelligent systems.

You: Who invented AI?
Bot: AI was first introduced by John McCarthy in the 1950s.

You: Thank you!
Bot: You're welcome!

🤝 Contributing
Pull requests are welcome! If you find a bug or want to suggest improvements, feel free to open an issue or PR.
