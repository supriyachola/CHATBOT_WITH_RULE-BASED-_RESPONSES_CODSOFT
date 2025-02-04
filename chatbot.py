import tkinter as tk
from tkinter import scrolledtext

# Dictionary with predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm ChatBot, your virtual assistant!",
    "bye": "Goodbye! Have a great day!",
    "who created you": "I was created by an AI enthusiast!",
    "default": "I'm not sure about that. Can you rephrase?"
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

# Function to handle send button
def send_message(event=None):
    user_input = entry.get()
    if user_input:
        chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
        bot_response = get_response(user_input)
        chat_window.insert(tk.END, "Bot: " + bot_response + "\n", "bot")
        entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Rule-Based ChatBot")
root.geometry("400x500")
root.configure(bg="#222831")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.pack(pady=10)
chat_window.tag_config("user", foreground="#00adb5")
chat_window.tag_config("bot", foreground="black")  # Bot text color set to black

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12, "bold"),
                        bg="#00adb5", fg="white", padx=10, pady=5)
send_button.pack()

# Bind Enter key to send message
root.bind("<Return>", send_message)

root.mainloop()
