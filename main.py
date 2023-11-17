import matplotlib.pyplot as plt
import numpy as np

# Define the coefficients a and b for your elliptic curve equation
a = 1
b = 1

# Generate x values
x = np.linspace(-2, 2, 400)
# Calculate y values using the elliptic curve equation
y_positive = np.sqrt(x**3 + a*x + b)
y_negative = -np.sqrt(x**3 + a*x + b)

# Plot the positive and negative branches of the curve
plt.plot(x, y_positive, label='y = √(x^3 + ax + b)')
plt.plot(x, y_negative, label='y = -√(x^3 + ax + b)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Elliptic Curve: y^2 = x^3 + ax + b')

# Add a legend
plt.legend()

# Show the plot
plt.grid()
plt.show()

