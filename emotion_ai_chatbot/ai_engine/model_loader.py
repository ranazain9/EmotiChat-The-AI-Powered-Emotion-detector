from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig
from accelerate import init_empty_weights, load_checkpoint_and_dispatch
import os

def load_openchat_model(local_path="./openchat_model", model_name="openchat/openchat-3.5-1210"):
    # ✅ STEP 1: Download model and tokenizer if not already saved
    if not os.path.exists(local_path):
        print("🔽 Downloading model...")

        # Load and save tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.save_pretrained(local_path)

        # 🔑 Load and save config explicitly (fixes model_type issue)
        config = AutoConfig.from_pretrained(model_name)
        config.save_pretrained(local_path)

        # Load and save model
        model = AutoModelForCausalLM.from_pretrained(model_name, config=config)
        model.save_pretrained(local_path)

        print("✅ Model downloaded and saved to:", local_path)

    # ✅ STEP 2: Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(local_path)

    # ✅ STEP 3: Load model using offload strategy
    print("⚙️ Loading model with disk offload...")
    with init_empty_weights():
        model = AutoModelForCausalLM.from_pretrained(local_path)

    model = load_checkpoint_and_dispatch(
        model,
        local_path,
        device_map="auto",
        offload_folder="offload_dir",
        offload_state_dict=True
    )

    return model, tokenizer

# Run directly (test only)
if __name__ == "__main__":
    model, tokenizer = load_openchat_model()
    print("🚀 Model and tokenizer are ready!")
