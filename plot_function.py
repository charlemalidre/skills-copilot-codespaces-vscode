import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
  return x**4 - 2*x**2 - 6

# Generate x values
x = np.linspace(-2.5, 2.5, 400)

# Calculate y values
y = f(x)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the function
plt.plot(x, y, label='f(x) = x⁴ - 2x² - 6')

# Mark local minima
plt.scatter([-1, 1], [-7, -7], color='red', label='Local Minima')
plt.text(-1, -7.5, '(-1, -7)')
plt.text(1, -7.5, '(1, -7)')

# Mark local maximum
plt.scatter([0], [-6], color='blue', label='Local Maximum')
plt.text(0, -5.5, '(0, -6)')

# Mark inflection points
inflection_x = [-1/np.sqrt(3), 1/np.sqrt(3)]
inflection_y = [f(val) for val in inflection_x]
plt.scatter(inflection_x, inflection_y, color='green', label='Inflection Points')
plt.text(inflection_x[0], inflection_y[0] + 0.5, f'(-1/√3, -59/9)')
plt.text(inflection_x[1], inflection_y[1] + 0.5, f'(1/√3, -59/9)')

# Mark y-intercept
plt.scatter([0], [-6], color='purple', label='Y-intercept') # Note: Same as local max
plt.text(0.1, -6, '(0, -6) Y-intercept')


# Mark x-intercepts
x_intercept_positive = np.sqrt(1 + np.sqrt(7))
x_intercept_negative = -np.sqrt(1 + np.sqrt(7))
plt.scatter([x_intercept_positive, x_intercept_negative], [0, 0], color='orange', label='X-intercepts')
plt.text(x_intercept_positive, 0.5, f'(√(1+√7), 0)')
plt.text(x_intercept_negative, 0.5, f'(-√(1+√7), 0)')

# Set title and labels
plt.title('Graph of f(x) = x⁴ - 2x² - 6')
plt.xlabel('x')
plt.ylabel('f(x)')

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Save the plot
plt.savefig('function_a_plot.png')

# Print success message
print("Plot created and saved as function_a_plot.png")

plt.show() # Optional: show the plot
