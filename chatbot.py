import json
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
data = pd.read_csv("questions.csv", usecols=[1, 2], names=["question1", "answer"], skiprows=1)
data.dropna(inplace=True)

# Ensure correct column names
if "question1" not in data.columns or "answer" not in data.columns:
    raise ValueError("CSV file must contain 'question1' and 'answer' columns.")

# Extract Questions & Answers
all_questions = data["question1"].astype(str).str.lower().tolist()
all_answers = data["answer"].astype(str).tolist()

# Train TF-IDF Model
vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(all_questions)

# Flask App
app = Flask(__name__, template_folder="chatbot_ui")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Invalid request. Please provide a 'question' key."}), 400
    
    user_input = data["question"].strip().lower()
    input_vector = vectorizer.transform([user_input])

    # Find Similar Question
    similarities = cosine_similarity(input_vector, question_vectors).flatten()
    
    if similarities.max() == 0:
        response = "I'm not sure about that. Can you rephrase your question?"
    else:
        best_match_idx = np.argmax(similarities)
        response = all_answers[best_match_idx]

    return jsonify({"answer": response})  # Ensure JSON key is 'answer'


# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)