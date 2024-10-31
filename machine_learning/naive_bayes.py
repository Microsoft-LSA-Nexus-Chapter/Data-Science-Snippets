# -*- coding: utf-8 -*-
"""Naive_Bayes.py


#Naive Bayes clasification .
## Project By: Aditya Ghosh
[Linkedin](https://www.linkedin.com/in/adityaghosh2992/) [Github](https://github.com/aditya-ghosh2992)


"""

# Naive Bayes clasification .
## Make a ML program to predict the similarity

# Sample Test : "__name__" and "__main__"

import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        # Number of samples and features
        n_samples, n_features = X.shape
        # Get unique class labels
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        # Initialize mean, variance, and prior probability for each class
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.zeros(n_classes, dtype=np.float64)

        # Calculate statistics for each class
        for idx, c in enumerate(self._classes):
            X_c = X[y == c]  # Samples belonging to class c
            self._mean[idx, :] = X_c.mean(axis=0)  # Mean for each feature
            self._var[idx, :] = X_c.var(axis=0)    # Variance for each feature
            self._priors[idx] = X_c.shape[0] / float(n_samples)  # Prior probability

    def predict(self, X):
        # Predict class for each sample in X
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Calculate posterior probability for each class and choose the class with the highest probability
        posteriors = []

        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx])  # Prior probability in log form
            posterior = np.sum(np.log(self._pdf(idx, x)))  # Likelihood in log form
            posterior = prior + posterior  # Posterior (log-prior + log-likelihood)
            posteriors.append(posterior)

        # Return the class with the highest posterior probability
        return self._classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        # Probability Density Function (PDF) for Gaussian distribution
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(-((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator


# Testing the Naive Bayes classifier
if __name__ == "__main__":
    # Imports
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    # Helper function to calculate accuracy
    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    # Generate a sample dataset
    X, y = datasets.make_classification(
        n_samples=1000, n_features=10, n_classes=2, random_state=123
    )

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123
    )

    # Initialize and train the Naive Bayes model
    nb = NaiveBayes()
    nb.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = nb.predict(X_test)

    # Print accuracy
    print("Naive Bayes classification accuracy:", accuracy(y_test, predictions))

