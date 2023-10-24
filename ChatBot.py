# ChatBot responses
answers = {
    "hi": "Hello! How can I help you?",
    "how are you?": "I am just a computer programm, so I have no feelings, but thanks for asking!",
    "what's your name?": "I am a ChatBot.",
    "goodbye": "See you later!",
}

# Processing user message and preparing an answer
def responder(message):
    message = message.lower()  # Converting message to lowercase
    if message in answers:
        return answers[message]
    else:
        return "Sorry, I did not understand."

# Chatbot loop
while True:
    message = input("You: ")
    if message.lower() == "exit":
        print("Chatbot: Bye!")
        break
    answer = responder(message)
    print("Chatbot:", answer)
