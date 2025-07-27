# ai_engine/emotion_detector.py
from transformers import pipeline
import warnings

# Optional: suppress future deprecation warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# Import necessary libraries

# Load pre-trained emotion classification pipeline
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base",  top_k=None)

def detect_emotion(text):
    """
    Detect the dominant emotion in the given text using a pre-trained transformer.
    Returns: (emotion_label, confidence_score)
    """
    results = emotion_classifier(text)[0]  # Get list of emotion scores
    results.sort(key=lambda x: x['score'], reverse=True)  # Sort by score descending
    top_emotion = results[0]
    return top_emotion['label'], top_emotion['score']



if __name__ == "__main__":
    sample_text = "I am so happy to see you!"
    emotion, confidence = detect_emotion(sample_text)
    print(f"Detected Emotion: {emotion}, Confidence: {confidence:.2f}")
# This code defines a simple emotion detection function using a pre-trained transformer model.

