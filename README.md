# Emotion-Aware Chatbot

![Chatbot Demo](demo.gif)

An intelligent chatbot that detects user emotions from text input and provides empathetic responses using advanced NLP models.

## Features

- **Real-time Emotion Detection**: Identifies 6 core emotions (happy, sad, angry, fearful, surprised, neutral)
- **Contextual Response Generation**: Tailors responses based on detected emotion
- **Multi-Theme Interface**: Light, dark, blue, and pink color themes
- **Stress Management**: Special protocols for high-stress situations
- **Conversation Memory**: Maintains context during chats

## Technology Stack

### Frontend
- HTML5, CSS3, JavaScript
- jQuery for AJAX requests
- Tailwind CSS for styling

### Backend
- Django 4.2
- Django REST Framework

### NLP Models
- Emotion Detection: TextBlob + NLTK Vader
- Response Generation: Facebook's Blenderbot-small-90M

## System Architecture

```mermaid
graph TD
    A[User Input] --> B[Frontend]
    B -->|AJAX POST| C[Django Backend]
    C --> D[Emotion Detection]
    C --> E[Response Generation]
    D --> F[(TextBlob/NLTK)]
    E --> G[(Blenderbot)]
    F --> C
    G --> C
    C -->|JSON Response| B
