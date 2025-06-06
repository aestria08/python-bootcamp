from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()

# Load sentiment analysis model
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define input model
class UserInput(BaseModel):
    message: str

# Home route
@app.get("/")
def home():
    return {"message": "Mental Health Chatbot is running with FastAPI!"}

# Health check route
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Function to get sentiment
def get_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        output = model(**inputs)
    sentiment_scores = torch.nn.functional.softmax(output.logits, dim=-1)
    sentiment_index = sentiment_scores.argmax().item()

    sentiment_labels = ["Negative", "Neutral", "Positive"]
    return sentiment_labels[sentiment_index]

# Chatbot response route
@app.post("/predict")
def chatbot_response(user_input: UserInput):
    message = user_input.message.lower()
    sentiment = get_sentiment(message)  # Get sentiment from the model

    # Generate responses based on sentiment
    if sentiment == "Negative":
        response = "I'm sorry to hear that. You are not alone, and there are people who care about you. 💙"
    elif sentiment == "Neutral":
        response = "I see. If you want to talk more about it, I'm here to listen. 💬"
    elif sentiment == "Positive":
        response = "That's amazing to hear! Keep up the positive mindset. 😊"
    else:
        response = "I'm here to listen. Tell me more about what's on your mind. 💡"

    return {"sentiment": sentiment, "response": response}



# Function to generate chatbot response based on sentiment
def generate_response(sentiment):
    responses = {
        "Anxiety (Mild)": "I sense a little anxiety. Try taking a deep breath and focusing on something positive. 🌿",
        "Anxiety (Moderate)": "You're feeling anxious. Guided meditation or talking to someone can help. 💙",
        "Anxiety (Severe)": "You seem really anxious. Please know you're not alone—consider seeking professional support. 🫂",

        "Depression (Mild)": "Feeling a bit low? Sometimes, a small change in routine can make a big difference. 🌞",
        "Depression (Moderate)": "It sounds like you're struggling. Try journaling or talking to someone you trust. ❤️",
        "Depression (Severe)": "You're feeling deeply depressed. Remember, seeking support is a sign of strength. 🏡",

        "Neutral": "Got it! Let me know if you want to talk about something.",
        "Positive": "That's wonderful! Keep embracing the positive moments. 😊"
    }

    return responses.get(sentiment, "I'm here to listen. Tell me more about what's on your mind. 💬")


# Chatbot response route
@app.post("/predict")
def chatbot_response(user_input: UserInput):
    user_id = user_input.user_id
    message = preprocess_text(user_input.message)

    # Analyze sentiment
    sentiment = get_sentiment(message)

    # Track user sentiment history
    user_history = track_user_sentiment(user_id, sentiment)

    # Generate response
    chatbot_reply = generate_response(sentiment)

    return {
        "user_id": user_id,
        "user_message": user_input.message,
        "detected_sentiment": sentiment,
        "chatbot_response": chatbot_reply,
        "user_sentiment_history": user_history
    }
