# CHATBOT_WITH_RULE-BASED-_RESPONSES_CODSOFT
simple rule-based chatbot created using Python and Tkinter. The chatbot responds to user inputs based on predefined rules and patterns. It is an interactive assistant that can respond to common questions and provide useful feedback.



Features
- Rule-Based Responses: The chatbot identifies user queries using basic keyword matching and provides predefined responses.
- Interactive GUI: The chatbot has a GUI built with Tkinter, where users can type messages and receive responses.
- Pattern Matching: The bot matches specific words or phrases in user input and responds accordingly.
- User-Friendly Interface: Simple and clean interface for easy communication.

Requirements
Before running the application, ensure you have the following Python libraries installed:
- `tkinter` (usually comes pre-installed with Python)
- `scrolledtext` (part of `tkinter`)



 Code Explanation

- The chatbot matches predefined keywords (e.g., "hello", "how are you") in the user input.
- It uses simple `if-else` statements to determine which response to return.
- The Tkinter GUI is used to handle user interaction, displaying the conversation in a scrollable window.

 Key Sections in the Code:

- get_response(user_input): This function takes the user's input and matches it with predefined keywords to generate an appropriate response.
- send_message(): Handles sending the message from the user to the bot and displaying the response in the chat window.
- Tkinter Setup: Creates the GUI where the user can enter messages and interact with the chatbot.

 Example Interaction:

1. User: "hello"
   - Bot: "Hello! How can I assist you today?"

2. User: "who created you"
   - Bot: "I was created by an AI enthusiast!"

3. User: "how are you"
   - Bot: "I'm just a bot, but I'm doing great! How about you?"

4. User: "bye"
   - Bot: "Goodbye! Have a great day!"



