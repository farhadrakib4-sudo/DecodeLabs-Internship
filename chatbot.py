print(" Rule-Based Chatbot")
print("Type 'exit' to end the conversation.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "who created you":
        print("Bot: I was created using Python if-else statements.")

    elif user == "help":
        print("Bot: You can greet me, ask my name, ask how I am, or type 'exit'.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")