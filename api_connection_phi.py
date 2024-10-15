# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "hoa como estas?"},
]
pipe = pipeline("text-generation", model="microsoft/Phi-3.5-mini-instruct", framework="pt", trust_remote_code=True)

pipe(messages)