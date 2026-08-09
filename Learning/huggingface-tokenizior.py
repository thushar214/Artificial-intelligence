from huggingface_hub import login
from dotenv import load_dotenv
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

#Login to Hugging Face..
load_dotenv("../Aliens_force/keys.env")
HF=os.getenv("HF_TOKEN")
login(HF)
print("Logged in")

#Defining the model
model_name = 'meta-llama/Llama-3.1-8B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model_call = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16)
Inputs = 'What is AI. Explain me in simple terms'
inp = tokenizer(Inputs, return_tensors="pt").to(model_call.device)

print(inp)
outputs = model_call.generate(**inp, max_tokens=700, temperature=0.7)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))