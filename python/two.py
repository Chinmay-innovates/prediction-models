# Sample data
X = [1, 2, 3, 4, 5]  # Independent variable
Y = [3, 4, 2, 5, 6]  # Dependent variable

# Calculate the necessary values for the formulas
n = len(X)
sum_X = sum(X)
sum_Y = sum(Y)
sum_XY = sum(x * y for x, y in zip(X, Y))
sum_X2 = sum(x ** 2 for x in X)

# Calculate the slope (a) and intercept (b)
a = (n * sum_XY - sum_X * sum_Y) / (n * sum_X2 - sum_X ** 2)
b = (sum_Y * sum_X2 - sum_X * sum_XY) / (n * sum_X2 - sum_X ** 2)

# Print the results
print(f"Coefficient (slope): {a}")
print(f"Intercept: {b}")

# Predict Y values using the model
Y_pred = [a * x + b for x in X]

# Plotting the results
import matplotlib.pyplot as plt 

plt.scatter(X, Y, color='blue')  # Original data points
plt.plot(X, Y_pred, color='red')  # Regression line
plt.xlabel('X (Independent Variable)')
plt.ylabel('Y (Dependent Variable)')
plt.title('Simple Linear Regression (Without Predefined Functions)')
plt.show()
