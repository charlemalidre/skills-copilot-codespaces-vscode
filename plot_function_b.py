import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
  # Avoid division by zero at the asymptote
  with np.errstate(divide='ignore', invalid='ignore'):
    result = (x**2 - 1) / (4*x + 5)
    result[np.isinf(result)] = np.nan # Replace infinities with NaN
    result[np.abs(4*x + 5) < 1e-6] = np.nan # Explicitly handle asymptote
  return result

# Define the oblique asymptote function
def y_oblique(x):
  return (1/4)*x - 5/16

# Generate x values, avoiding the asymptote at x = -5/4 (-1.25)
x1 = np.linspace(-5, -1.25 - 1e-3, 200) # from -5 up to (but not including) -1.25
x2 = np.linspace(-1.25 + 1e-3, 5, 200)  # from (but not including) -1.25 up to 5
x_full = np.linspace(-5, 5, 400) # For the oblique asymptote

# Calculate y values
y1 = f(x1)
y2 = f(x2)
y_oblique_values = y_oblique(x_full)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot the function in two parts
plt.plot(x1, y1, label='f(x) = (x² - 1) / (4x + 5)', color='blue')
plt.plot(x2, y2, color='blue') # No label for the second part to avoid duplicate legend entry

# Plot vertical asymptote
plt.axvline(-5/4, color='gray', linestyle='--', label='Vertical Asymptote x = -5/4')

# Plot oblique asymptote
plt.plot(x_full, y_oblique_values, color='orange', linestyle='--', label='Oblique Asymptote y = x/4 - 5/16')

# Mark points
# Local maximum: (-2, -1)
plt.scatter([-2], [-1], color='red', zorder=5)
plt.text(-2, -1 - 0.3, '(-2, -1) Local Max', ha='center')

# Local minimum: (-1/2, -0.25)
plt.scatter([-0.5], [-0.25], color='green', zorder=5)
plt.text(-0.5, -0.25 + 0.2, '(-1/2, -0.25) Local Min', ha='center')

# Inflection point: (0.9, -19/860) approx (0.9, -0.022)
inflection_x = 0.9
inflection_y = (inflection_x**2 - 1) / (4*inflection_x + 5) # approx -0.022093
plt.scatter([inflection_x], [inflection_y], color='purple', zorder=5)
plt.text(inflection_x, inflection_y + 0.2, f'({inflection_x:.1f}, {inflection_y:.3f}) Inflection Pt', ha='center')

# Y-intercept: (0, -0.2)
y_intercept_y = (0**2 - 1) / (4*0 + 5) # -1/5 = -0.2
plt.scatter([0], [y_intercept_y], color='cyan', zorder=5)
plt.text(0, y_intercept_y - 0.3, f'(0, {y_intercept_y:.1f}) Y-intercept', ha='center')

# X-intercepts: (1, 0) and (-1, 0)
plt.scatter([1, -1], [0, 0], color='magenta', zorder=5)
plt.text(1, 0 + 0.2, '(1, 0) X-intercept', ha='center')
plt.text(-1, 0 + 0.2, '(-1, 0) X-intercept', ha='center')

# Set title and labels
plt.title('Graph of f(x) = (x² - 1) / (4x + 5)')
plt.xlabel('x')
plt.ylabel('f(x)')

# Add grid
plt.grid(True)

# Add legend
plt.legend(loc='upper left')

# Adjust ylim
plt.ylim(-5, 5)

# Save the plot
plt.savefig('function_b_plot.png')

# Print success message
print("Plot created and saved as function_b_plot.png")

# plt.show() # Optional: show the plot
