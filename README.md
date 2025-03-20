# FAQ Chatbot

## Overview
This is a simple FAQ chatbot built using Flask and TF-IDF for text similarity matching. It loads frequently asked questions from a CSV file and responds to user queries with the most relevant answer. If no close match is found, it prompts the user to rephrase their question.

## Features
- **Natural Language Processing**: Uses TF-IDF and cosine similarity to match user queries.
- **Flask Web Server**: Serves as the backend for handling requests.
- **Interactive Web UI**: Simple and clean chatbot interface built with HTML, CSS, and JavaScript.
- **Scalable Data Handling**: Loads and processes questions from a CSV file.

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Flask
- Pandas
- Scikit-learn
- Numpy

## Running the Chatbot
Start the Flask server with:
```bash
python chatbot.py
```
The chatbot will be available at `http://127.0.0.1:5000/`.

## API Endpoint
- **POST `/chat`**: Accepts a JSON payload `{ "question": "your question" }` and returns an answer.

## Folder Structure
```
faq-chatbot/
│-- chatbot_ui/ index.html       # Frontend (HTML, CSS, JS)
│-- questions.csv      # FAQ dataset
│-- chatbot.py             # Flask backend

```

## Future Improvements
- Integrate an AI-powered response generator (e.g., GPT-3.5) for better handling of unknown questions.
- Implement a database instead of a CSV file for better scalability.
- Add user authentication for personalized chatbot interactions.


![Screenshot 2025-03-20 133458](https://github.com/user-attachments/assets/16c1a374-cece-494a-ab73-6bb6b457270d)
![Screenshot 2025-03-20 133530](https://github.com/user-attachments/assets/443824bf-f11f-46db-9c98-7b6d03c4c369)

