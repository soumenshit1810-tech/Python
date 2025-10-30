while True:
    user = input("You: ").lower()
    if "hello" in user:
        print("Bot: Hi there!")
    elif "how are you" in user:
        print("Bot: I'm just code, but I'm fine 😄")
    elif "bye" in user:
        print("Bot: Goodbye 👋")
        break
    else:
        print("Bot: Sorry, I didn’t understand that.")
