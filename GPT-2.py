# Import necessary libraries
from transformers import pipeline, set_seed

# Set seed for reproducibility
set_seed(42)

# Load the pre-trained GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Define a function to generate responses
def generate_response(prompt, max_length=100):
    response = generator(prompt, max_length=max_length, do_sample=True, temperature=0.7)[0]['generated_text']
    return response.strip()

# Set up the chatbot loop
while True:
    # Get user input
    user_input = input("You: ")

    # Generate a response
    chatbot_response = generate_response(user_input)

    # Print the chatbot response
    print("Chatbot: " + chatbot_response)
