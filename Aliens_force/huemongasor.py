from dotenv import load_dotenv
import os
from huggingface_hub import login
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

load_dotenv("keys.env")
HF=os.getenv("HF_TOKEN")
login(HF)

# Transformers_mdl=pipeline("text-generation", model="gpt2")
# print(Transformers_mdl("How AI will change the world"))
model = "deepseek-ai/deepseek-coder-1.3b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForCausalLM.from_pretrained(model)

prompt = """
Convert this python code to Rust     code to make faster execution

python code :
def fibonacci(n):
    if n <= 1:
        return n
    # The logic splits into two branches every time, causing O(2^n) growth
    return fibonacci(n-1) + fibonacci(n-2)

n_terms = 40
print(f"Calculating Fibonacci term {n_terms}...")
result = fibonacci(n_terms)
print(f"Result: {result}")

"""

inputs=tokenizer(prompt, return_tensors="pt")
outputs=model.generate(**inputs, max_new_tokens=250)

resp = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(resp)
res  = resp.split("```")[1].replace("cpp","").strip()
print(res)
