import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# create dataset
# Sample data (Size, Bedrooms, Age)
# Number of data points
n = 100

# Generate random data
# House sizes between 500 and 5000 square feet
sizes = np.random.randint(500, 5000, n)

# Number of bedrooms between 1 and 7
bedrooms = np.random.randint(1, 7, n)

# House age between 0 and 100 years
ages = np.random.randint(0, 100, n)

# Base price formula (just for the sake of generating data)
prices = (sizes * 100) + (bedrooms * 5000) - (ages * 200) + np.random.randint(-20000, 20000, n)

# Create a DataFrame
data = pd.DataFrame({
    'Size': sizes,
    'Bedrooms': bedrooms,
    'Age': ages,
    'Price': prices
})

# Display the first few rows
print(data.head())
data.to_csv('house_prices_large_dataset.csv', index=False)
df = pd.DataFrame(data)

# pre the data
X = df[['Size', 'Bedrooms', 'Age']]  # Features
Y = df['Price']  # Target

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#create and train the modal
# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, Y_train)

#make predictions
# Predict prices on the test data
Y_pred = model.predict(X_test)

# Calculate the mean squared error and R^2 score
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Output the coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


#ploting origina
plt.scatter(Y_test, Y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.show()
