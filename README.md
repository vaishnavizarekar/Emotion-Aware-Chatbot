# Emotion-Aware Chatbot

An AI-powered conversational chatbot that detects emotions in user messages and generates context-aware responses using Hugging Face Transformers and a locally running Gemma 2B model through Ollama.

## Overview

The Emotion-Aware Chatbot is a web-based application developed using Python and Flask. It analyses the emotional tone of user messages and adapts chatbot responses accordingly.

The application uses a pretrained DistilRoBERTa emotion classification model to identify emotions and Ollama's Gemma 2B model to generate conversational responses.

## Features

- **Emotion Detection:** Identifies emotions in text using a pretrained Hugging Face model.
- **Context-Aware Responses:** Generates responses based on detected emotions.
- **Interactive Chat Interface:** Provides a browser-based chatbot interface.
- **Voice Input:** Supports speech recognition through the browser's Web Speech API.
- **Text-to-Speech:** Reads chatbot responses aloud.
- **Chat History:** Stores previous chat sessions in browser local storage.
- **Feedback System:** Allows users to provide positive or negative feedback.
- **Export Chat:** Allows users to download the current conversation.
- **Dark Mode:** Provides a dark-mode interface option.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Emotion Detection | Hugging Face Transformers |
| Emotion Model | j-hartmann/emotion-english-distilroberta-base |
| Response Generation | Ollama |
| Language Model | Gemma 2B |
| Browser Features | Web Speech API, Local Storage |

## How It Works

1. The user enters a message through the chatbot interface.
2. The Flask backend receives the message.
3. The emotion detection pipeline analyses the text using DistilRoBERTa.
4. The detected emotion determines the response prompt.
5. The prompt is sent to the locally running Gemma 2B model through Ollama.
6. The generated response is returned to the frontend.
7. The chatbot displays and optionally speaks the response.

## Project Structure

```text
Emotion-Aware-Chatbot/
│
├── app.py
├── chatbot.py
├── index.js
├── intents.json
├── requirements.txt
├── q_table_log.txt
│
├── templates/
│   └── index.html
│
├── static/
│
└── logs/
```

## Installation and Setup

### Prerequisites

- Python
- pip
- Ollama

### 1. Clone the repository

```bash
git clone https://github.com/vaishnavizarekar/Emotion-Aware-Chatbot.git

cd Emotion-Aware-Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The dependencies must include Flask, Requests, Transformers and PyTorch.

### 4. Download the Gemma model

```bash
ollama pull gemma:2b
```

Ensure the Ollama service is running locally.

### 5. Run the application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Current Implementation Notes

- Emotion classification uses a pretrained DistilRoBERTa model.
- Response generation uses Gemma 2B through the local Ollama API.
- Chat sessions are stored in browser local storage.
- Feedback is recorded in a local log file.
- The current implementation does not include Azure or Google Cloud emotion detection, database-backed chat history, authentication, or a trained reinforcement-learning algorithm.

## Future Improvements

- Implement actual reinforcement learning based on user feedback.
- Add persistent conversation storage using a database.
- Improve emotion classification and response handling.
- Add user authentication and secure session management.
- Introduce automated unit and integration testing.

## Repository

GitHub: https://github.com/vaishnavizarekar/Emotion-Aware-Chatbot
