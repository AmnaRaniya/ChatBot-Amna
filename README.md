# ChatBot-Amna
Artificial Intelligence Task 1 by decode Labs
PROJECT 1: Rule-Based AI Chatbot
================================

Author: Amna Bibi
Description: A chatbot that responds to predefined user inputs using a dictionary lookup.


TABLE OF CONTENTS
-----------------
1. What This Chatbot Does
2. All Available Commands
3. How to Run the Program
4. How the Code Works
5. Complete Code Listing
6. Sample Conversation
7. Modifying the Bot


1. WHAT THIS CHATBOT DOES
-------------------------

This is a simple rule-based chatbot. It:
- Takes text input from the user
- Converts input to lowercase for matching
- Looks up the input in a dictionary of predefined responses
- Returns the matching response
- If no match is found, returns a default "I don't understand" message
- Ends conversation when user types: quit, exit, bye, or goodbye


2. ALL AVAILABLE COMMANDS
-------------------------

TYPE THIS:              THE BOT WILL SAY:
-------------------     --------------------------------------------------
hello                   Hello! Welcome to DecodeLabs ChatBot. How can I help you today?

hi                      Hi there! Great to see you.

hey                     Hey! Ready to learn some AI?

how are you             I'm functioning perfectly! Thanks for asking.

what is your name       I'm Project 1 ChatBot developed by Amna, your rule-based assistant.

who made you            I was built by an AI engineer 'Amna Bibi' at DecodeLabs.

help                    I understand: greetings (hello/hi/hey), 'how are you',
                        'what is your name', 'who made you', and 'bye'. Try me!

joke                    Why did the programmer quit his job? Because he didn't get arrays!

quote                   The best way to predict the future is to build it. - Alan Kay

bye                     Goodbye! Thanks for chatting. Come back soon!

goodbye                 See you later! Keep coding!

exit                    Exiting chat. Have a great day!

ANYTHING ELSE           Sorry, I don't understand '______'. Type 'help' to see what I can do.

EXIT WORDS (quit, exit, bye, goodbye) - Ends the program


3. HOW TO RUN THE PROGRAM
-------------------------

REQUIREMENTS:
- Python 3.x installed on your computer
- No additional libraries needed (uses only built-in Python)

STEPS:
1. Save the code in a file called chatbot.py
2. Open terminal or command prompt
3. Navigate to the folder containing chatbot.py
4. Type: python chatbot.py
5. Press Enter
6. Start chatting!


4. HOW THE CODE WORKS
---------------------

The program follows this exact sequence:

STEP 1: Create a dictionary called 'responses'
        - Keys are user inputs (lowercase)
        - Values are bot replies

STEP 2: Create a list called 'exit_words'
        - Contains: "quit", "exit", "bye", "goodbye"

STEP 3: Print welcome message with instructions

STEP 4: Start an infinite while loop

        Inside the loop:
        
        A. Get user input with input("You: ")
        
        B. Clean the input:
           - Convert to lowercase using .lower()
           - Remove extra spaces using .strip()
        
        C. Check if input is empty:
           - If yes, print "You didn't type anything!" and restart loop
        
        D. Check if input is in exit_words:
           - If yes, print goodbye message and break the loop
        
        E. Look up response in dictionary:
           - Use .get() method
           - If found, return the response
           - If not found, return fallback message
        
        F. Print the bot's response


5. COMPLETE CODE LISTING
------------------------

Here is the exact code from the project:

```python
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
6.	SAMPLE CONVERSATION
________________________________________
Here is what happens when you run the program:
================================================================
🤖 CHATBOT READY 🤖
================================================================
Type 'help' to see what I can do.
Type 'quit' or 'bye' to end the conversation.
================================================================
You: hello
Bot: Hello! Welcome to DecodeLabs ChatBot. How can I help you today?
You: who made you
Bot: I was built by an AI engineer 'Amna Bibi' at DecodeLabs.
You: tell me a joke
Bot: Sorry, I don't understand 'tell me a joke'. Type 'help' to see what I can do.
You: joke
Bot: Why did the programmer quit his job? Because he didn't get arrays!
You: help
Bot: I understand: greetings (hello/hi/hey), 'how are you', 'what is your name', 'who made you', and 'bye'. Try me!
You: bye
Bot: Goodbye! Thanks for chatting. Come back soon!
================================================================
👋 CHAT ENDED 👋
================================================================
7.	MODIFYING THE BOT
________________________________________
ADDING NEW RESPONSES:
________________________________________
Edit the 'responses' dictionary. Add a line like this:
"your keyword": "your bot response",
Example - add weather response:
"weather": "I don't know the weather, but it's always sunny in code!",
ADDING NEW EXIT WORDS:
________________________________________
Add words to the 'exit_words' list:
exit_words = ["quit", "exit", "bye", "goodbye", "cya", "adios"]
CHANGING THE FALLBACK MESSAGE:
________________________________________
Edit the second argument in .get() method:
reply = responses.get(clean_input, "YOUR NEW FALLBACK MESSAGE HERE")
END OF DOCUMENT

