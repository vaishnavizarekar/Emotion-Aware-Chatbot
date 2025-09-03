import requests
from transformers import pipeline

# Load HuggingFace emotion detection model
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

# Simple Q-table as a dictionary
q_table = {}  # {(state, action): value}

def detect_emotion(user_input):
    result = classifier(user_input)
    return result[0][0]['label'].lower()  # e.g., joy, sadness, anger

def get_bot_response(user_input):
    emotion = detect_emotion(user_input)

    if emotion == "joy":
        prompt = f"The user is feeling joyful. Respond enthusiastically to: {user_input}"
    elif emotion == "sadness":
        prompt = f"The user is feeling sad. Respond with empathy to: {user_input}"
    elif emotion == "anger":
        prompt = f"The user is angry. Respond calmly and helpfully to: {user_input}"
    else:
        prompt = f"Respond neutrally to: {user_input}"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return "Sorry, something went wrong with the model."
    except Exception as e:
        return f"Error: {e}"

def update_q_table(feedback_text):
    print(f"Feedback received: {feedback_text}")
    with open("q_table_log.txt", "a") as file:
        file.write(f"{feedback_text}\n")