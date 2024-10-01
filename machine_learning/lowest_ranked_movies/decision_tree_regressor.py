import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state = 3)
movies = pd.read_csv('machine_learning/lowest_ranked_movies/movies.csv')
temp = ["duration" , "review_count"]
X = movies[temp]
y = movies.rating

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 10)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
accuracy = mean_absolute_error(y_test, y_pred)
print(f"accuracy of the model : {accuracy*100: .3f}")