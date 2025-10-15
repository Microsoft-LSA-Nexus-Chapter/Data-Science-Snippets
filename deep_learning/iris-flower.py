# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

# Features and labels
X = iris.data          # Sepal and petal measurements
y = iris.target        # Flower species (0, 1, 2)

# Split data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Try predicting a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example flower measurements
predicted_class = iris.target_names[model.predict(sample)[0]]
print(f"Predicted Flower Species: {predicted_class}")
