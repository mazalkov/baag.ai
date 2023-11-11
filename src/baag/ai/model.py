import openai
from keys import OPEN_API_KEY

# Set your API key
openai.api_key = OPEN_API_KEY

# Define the model you want to use (e.g., "text-davinci-003")
model_name = "text-davinci-003"


def summarise(prompt: str) -> str:
    # Get the response from the model
    response = openai.Completion.create(model=model_name, prompt=prompt, max_tokens=60)

    return response.choices[0].text.strip()
