from transformers import BlenderbotSmallTokenizer, BlenderbotSmallForConditionalGeneration
import torch

# Load model only once when the app starts
tokenizer = None
model = None

def load_model():
    global tokenizer, model
    if tokenizer is None or model is None:
        tokenizer = BlenderbotSmallTokenizer.from_pretrained("facebook/blenderbot_small-90M")
        model = BlenderbotSmallForConditionalGeneration.from_pretrained("facebook/blenderbot_small-90M")

def generate_response(user_message, emotion):
    load_model()
    
    try:
        # Format input with emotion context
        input_text = f"[User is feeling {emotion}] {user_message}"
        
        inputs = tokenizer(input_text, return_tensors="pt")
        
        outputs = model.generate(
            **inputs,
            max_length=100,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2
        )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
        
    except Exception as e:
        print(f"Error generating response: {e}")
        return "I'm having trouble understanding. Could you rephrase that?"

