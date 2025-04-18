import numpy as np
from sklearn.linear_model import LinearRegression

# Given dataset
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Reshape for sklearn
y = np.array([2, 4, 5, 4, 5])

# Create and train the model
model = LinearRegression()
model.fit(x, y)

# Predict the sixth value (x = 6)
predicted_value = model.predict(np.array([[6]]))
print(f"The predicted value for x=6 is: {predicted_value[0]}")
