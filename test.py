import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()



XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "system", "content": "You are a sentiment analyzer and general analyst."},
        {"role": "user", "content": "Tell me about @infocyde posted about on X over the last 24 hours?"},
    ],
    temperature=0.01,
)

# print(completion.choices[0].message)
print(f"{completion}")