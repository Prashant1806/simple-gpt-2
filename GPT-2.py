# Import necessary libraries
import tkinter as tk
from transformers import pipeline, set_seed

# Set seed for reproducibility
set_seed(42)

# Load the pre-trained GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Define a function to generate responses
def generate_response(prompt, max_length=100):
    response = generator(prompt, max_length=max_length, do_sample=True, temperature=0.7)[0]['generated_text']
    return response.strip()

# Define function to handle user input
def send_message(event=None):
    # Get user input from entry widget
    user_input = user_input_entry.get()
    user_input_entry.delete(0, tk.END)

    # Generate a chatbot response
    chatbot_response = generate_response(user_input)

    # Add user input and chatbot response to the chatbox
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, "You: " + user_input + "\n\n")
    chatbox.insert(tk.END, "Chatbot: " + chatbot_response + "\n\n")
    chatbox.config(state=tk.DISABLED)
    chatbox.see(tk.END)

# Set up GUI
root = tk.Tk()
root.title("Generative Transformer Chatbot")

# Add chatbox
chatbox = tk.Text(root, height=20, width=50, state=tk.DISABLED)
chatbox.pack(padx=10, pady=10)

# Add user input entry widget
user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack(padx=10, pady=10)
user_input_entry.bind("<Return>", send_message)

# Add send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Start GUI main loop
root.mainloop()
