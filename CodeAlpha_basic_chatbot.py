print("Welcome to the Basic Chatbot!")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You:").lower()  # Take input and convert to lowercase

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hi there! " )
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks! How about you?")
    elif user_input in ["i am fine", "i’m fine", "good", "great"]:
        print("Bot: That’s nice to hear! ")
    elif user_input == "what is your name":
        print("Bot: I’m CodeBuddy, your friendly chatbot.")
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: Sorry, I didn’t understand that. Try saying 'hello' or 'how are you'.")