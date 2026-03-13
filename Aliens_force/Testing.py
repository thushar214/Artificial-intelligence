from transformers import pipeline
from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv("../Aliens_force/keys.env")
HF=os.getenv("HF_TOKEN")
login(HF)

generator = pipeline(
    "text-generation",
    model="gpt2"
)

prompt='What is music'

res=generator(prompt, max_length=50)

print(res[0]["generated_text"])
