import torch
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline


login(token="HUGGING_FACE_API_KEY")

model_id="google/gemma-3-270m-it"
print("Loading Model")

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id,dtype = torch.float32,device_map = "cpu")

print("Model Loaded Successfully")

chat_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=20,
    temperature=0.5,
    repetition_penalty=1.1
)
print("success")