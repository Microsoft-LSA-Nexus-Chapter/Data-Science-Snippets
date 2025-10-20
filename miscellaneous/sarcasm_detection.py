import json
import re
import string
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load dataset (example: News Headlines dataset for Sarcasm Detection)
# Downloadable from: https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection
data = []
with open("Sarcasm_Headlines_Dataset.json", "r") as f:
    for line in f:
        data.append(json.loads(line))

df = pd.DataFrame(data)
print("Sample data:\n", df.head())

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()

df["headline"] = df["headline"].apply(clean_text)

# Features and labels
X = df["headline"]
y = df["is_sarcastic"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Logistic Regression Model
model = LogisticRegression(max_iter=200)
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

# Evaluation
print("\nModel Performance:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict new samples
def predict_sarcasm(text):
    text_clean = clean_text(text)
    vec = vectorizer.transform([text_clean])
    pred = model.predict(vec)[0]
    return "Sarcastic 🤨" if pred == 1 else "Not Sarcastic 🙂"

# Example predictions
print("\nExamples:")
print("1:", predict_sarcasm("I absolutely love waiting in long queues!"))
print("2:", predict_sarcasm("The stock market is up again today."))
