import pandas as pd
from transformers import pipeline


# Initialize the AI model (using a pre-trained model from Hugging Face)
model = pipeline('text-generation', model='gpt2')

# Function to split data into chunks
def split_into_chunks(data, chunk_size):
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i:i + chunk_size])
    return chunks

# Function to generate responses based on prompts and data
def generate_response(prompt, data, max_length=1000, chunk_size=900):
    # Split the data into chunks
    data_chunks = split_into_chunks(data.to_string(), chunk_size)
    
    responses = []
    for chunk in data_chunks:
        full_prompt = f"{prompt}\n\n\n{chunk}"
        response = model(full_prompt, max_length=max_length, num_return_sequences=1)
        generated_text = response[0]['generated_text']
        response.append(generated_text)
    
    # Combine all responses
    final_response = " ".join(responses)
    

    return final_response

