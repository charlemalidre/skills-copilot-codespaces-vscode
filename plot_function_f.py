import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
  # Avoid division by zero at the asymptotes
  denominator = x**2 + x - 2
  with np.errstate(divide='ignore', invalid='ignore'):
    result = (x**2 + 4*x + 7) / denominator
    # Explicitly set NaN where denominator is close to zero
    result[np.abs(denominator) < 1e-6] = np.nan
  return result

# Generate x values in segments to handle discontinuities
x_points = 200 # Points per segment
x1 = np.linspace(-10, -2 - 1e-4, x_points)  # From -10 to just before -2
x2 = np.linspace(-2 + 1e-4, 1 - 1e-4, x_points) # From just after -2 to just before 1
x3 = np.linspace(1 + 1e-4, 10, x_points)   # From just after 1 to 10

# Calculate y values for each segment
y1 = f(x1)
y2 = f(x2)
y3 = f(x3)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot the function for each segment
plt.plot(x1, y1, label='f(x) = (x² + 4x + 7) / (x² + x - 2)', color='blue')
plt.plot(x2, y2, color='blue') # No label for the second part
plt.plot(x3, y3, color='blue') # No label for the third part

# Plot vertical asymptotes
plt.axvline(-2, color='gray', linestyle='--', label='Vertical Asymptote x = -2')
plt.axvline(1, color='gray', linestyle='--', label='Vertical Asymptote x = 1')

# Plot horizontal asymptote
plt.axhline(1, color='orange', linestyle='--', label='Horizontal Asymptote y = 1')

# Mark points
# Local minimum: (-5, 2/3)
local_min_x = -5
local_min_y = (local_min_x**2 + 4*local_min_x + 7) / (local_min_x**2 + local_min_x - 2) # 2/3
plt.scatter([local_min_x], [local_min_y], color='red', zorder=5)
plt.text(local_min_x, local_min_y - 0.5, f'({local_min_x}, {local_min_y:.2f}) Local Min', ha='center')

# Local maximum: (-1, -2)
local_max_x = -1
local_max_y = (local_max_x**2 + 4*local_max_x + 7) / (local_max_x**2 + local_max_x - 2) # -2
plt.scatter([local_max_x], [local_max_y], color='green', zorder=5)
plt.text(local_max_x, local_max_y + 0.5, f'({local_max_x}, {local_max_y}) Local Max', ha='center')

# Y-intercept: (0, -3.5)
y_intercept_x = 0
y_intercept_y = (y_intercept_x**2 + 4*y_intercept_x + 7) / (y_intercept_x**2 + y_intercept_x - 2) # 7 / -2 = -3.5
plt.scatter([y_intercept_x], [y_intercept_y], color='purple', zorder=5)
plt.text(y_intercept_x + 0.2, y_intercept_y, f'({y_intercept_x}, {y_intercept_y}) Y-intercept', va='center')

# Set title and labels
plt.title('Graph of f(x) = (x² + 4x + 7) / (x² + x - 2)')
plt.xlabel('x')
plt.ylabel('f(x)')

# Add grid
plt.grid(True)

# Add legend
plt.legend(loc='best')

# Adjust ylim to focus on the interesting parts of the graph
plt.ylim(-10, 10)

# Save the plot
plt.savefig('function_f_plot.png')

# Print success message
print("Plot created and saved as function_f_plot.png")

# plt.show() # Optional: show the plot
