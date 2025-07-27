from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "openchat/openchat-3.5-1210"


print("📦 Downloading model and tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)

tokenizer.save_pretrained("openchat_model")
model.save_pretrained("openchat_model")

print("✅ Download complete and saved to openchat_model/")
