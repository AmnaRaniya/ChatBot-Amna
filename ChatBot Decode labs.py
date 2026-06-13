"""
PROJECT 1: Rule-Based AI Chatbot
Author: Amna Bibi
Description: A chatbot that responds to predefined user inputs using a dictionary lookup.
"""

# ============================================
# KNOWLEDGE BASE - All the bot's responses
# ============================================

responses = {
    # Greetings
    "hello": "Hello! Welcome to DecodeLabs ChatBot. How can I help you today?",
    "hi": "Hi there! Great to see you.",
    "hey": "Hey! Ready to learn some AI?",
    
    # Questions about the bot
    "how are you": "I'm functioning perfectly! Thanks for asking.",
    "what is your name": "I'm Project 1 ChatBot developed by Amna, your rule-based assistant.",
    "who made you": "I was built by an AI engineer 'Amna Bibi' at DecodeLabs.",
    
    # Help and info
    "help": "I understand: greetings (hello/hi/hey), 'how are you', 'what is your name', 'who made you', and 'bye'. Try me!",
    
    # Fun responses
    "joke": "Why did the programmer quit his job? Because he didn't get arrays!",
    "quote": "The best way to predict the future is to build it. - Alan Kay",
    
    # Exit commands
    "bye": "Goodbye! Thanks for chatting. Come back soon!",
    "goodbye": "See you later! Keep coding!",
    "exit": "Exiting chat. Have a great day!"
}

# ============================================
# EXIT WORDS - What triggers the bot to stop
# ============================================

exit_words = ["quit", "exit", "bye", "goodbye"]

# ============================================
# BOT'S WELCOME MESSAGE
# ============================================

print("\n" + "="*50)
print("🤖 CHATBOT READY 🤖")
print("="*50)
print("Type 'help' to see what I can do.")
print("Type 'quit' or 'bye' to end the conversation.")
print("="*50 + "\n")

# ============================================
# MAIN LOOP - The heart of the chatbot
# ============================================

while True:
    # Step 1: Get input from user
    user_input = input("You: ")
    
    # Step 2: Clean the input (lowercase + remove spaces from ends)
    clean_input = user_input.lower().strip()
    
    # Step 3: Check if input is empty
    if clean_input == "":
        print("Bot: You didn't type anything! Try again.\n")
        continue  # Go back to the start of the loop
    
    # Step 4: Check if user wants to exit
    if clean_input in exit_words:
        print(f"Bot: {responses.get(clean_input, 'Goodbye!')}\n")
        print("="*50)
        print("👋 CHAT ENDED 👋")
        print("="*50)
        break  # Exit the loop and end the program
    
    # Step 5: Look up the response (or use fallback)
    reply = responses.get(clean_input, f"Sorry, I don't understand '{user_input}'. Type 'help' to see what I can do.")
    
    # Step 6: Print the bot's response
    print(f"Bot: {reply}\n")