import os
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import pipeline
import torch
from diffusers import StableDiffusionPipeline

load_dotenv("../Aliens_force/keys.env")
HF=os.getenv("HF_TOKEN")
login(HF)

# Transformer_pipeline= pipeline('sentiment-analysis')
# print(Transformer_pipeline('Today I got First rank at school, mom is going to be happy on this'))

# Transformer_pipelin = pipeline("zero-shot-classification")
# labels=["Moddy", "Happy","Sad"]
# print(Transformer_pipelin("Today I got the First rank in class.", candidate_labels=labels))

# ner=pipeline("token-classification",model="dslim/bert-base-NER", aggregation_strategy="simple")
# print(ner("The Apple Company share has been drop by 10% on today morning"))
#
# feature_extraction=pipeline("feature-extraction")
# print(feature_extraction("CPU is usage is excecced."))


