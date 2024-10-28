
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df = pd.read_csv('housing.csv')


df.fillna(df.mean(), inplace=True)


X = df[['feature1', 'feature2']] 
y = df['median_house_value']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


print(pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}).head())
