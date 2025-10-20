

import pandas as pd
import numpy as np
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Example dataset:
# You can use: https://www.kaggle.com/datasets/gyani95/380000-lyrics-from-metrolyrics
# For demo, create a small dataset
data = {
    "lyrics": [
        "I'm walking down the road with my guitar in the rain",
        "We light up the club till the sun goes down",
        "Tears falling down, love’s gone away",
        "You betrayed me, now I feel nothing inside",
        "Rage and thunder, fight till the end",
        "Calm wind and ocean waves, peaceful mind",
        "Money and fame, that's the game",
        "Let's dance all night, DJ play my favorite song"
    ],
    "genre": [
        "country", "pop", "pop", "rock", "metal", "jazz", "hiphop", "pop"
    ]
}

df = pd.DataFrame(data)

# Clean lyrics
def clean_lyrics(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()

df["lyrics"] = df["lyrics"].apply(clean_lyrics)

# Features and labels
X = df["lyrics"]
y = df["genre"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Naive Bayes Classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

print("\nModel Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Function to predict genre
def predict_genre(lyrics):
    lyrics_clean = clean_lyrics(lyrics)
    vec = vectorizer.transform([lyrics_clean])
    pred = model.predict(vec)[0]
    return pred.capitalize()

# Example predictions
print("\nExample Predictions:")
print("1:", predict_genre("Diamonds and cars, flashing lights everywhere"))
print("2:", predict_genre("My soul rests by the calm blue sea"))
print("3:", predict_genre("We rise and fight, we will never surrender"))
