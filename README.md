# simple-gpt-2
Python code example for building a generative transformer chatbot using the Hugging Face Transformers library








We import the required libraries, including the Hugging Face Transformers library, first in this code. Finally, we use the pipeline function to import the pre-trained GPT-2 model.

Then, using the GPT-2 model, we create a function called generate_response that accepts a prompt (the user's message) and produces a response. In order to create more varied and intriguing responses, we set the maximum length of the generated response to 100 and employ a sampling technique with a temperature of 0.7.

The generate_response function is then used in a loop to constantly ask the user for input and produce a response. The print function is used to output the chatbot answer to the console.
