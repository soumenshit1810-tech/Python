import aiml
import os
import sys

BRAIN_FILE = "bot_brain.brn"
AIML_FILE = "basic.aiml"

def create_kernel():
    kernel = aiml.Kernel()
    # If a saved brain exists, load it for fast startup
    if os.path.exists(BRAIN_FILE):
        kernel.bootstrap(brainFile=BRAIN_FILE)
    else:
        # Load all AIML files
        kernel.learn(AIML_FILE)
        # Optionally learn more files or directories:
        # kernel.learn("other.aiml")
        # Save compiled brain for next runs (faster)
        kernel.saveBrain(BRAIN_FILE)
    return kernel

def chat_loop(kernel):
    print("AIML bot ready. Type 'quit' or 'exit' to stop.")
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("Bot: Goodbye!")
            break
        # AIML expects uppercase patterns by default; kernel handles matching case-insensitively,
        # but it's common practice to send uppercase.
        response = kernel.respond(user_input)
        if not response:
            response = "Sorry, I don't know how to answer that yet."
        print("Bot:", response)

if __name__ == "__main__":
    kernel = create_kernel()
    chat_loop(kernel)
