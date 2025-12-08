import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 5*pi with step 0.1
x = np.arange(0, 5 * np.pi, 0.1)

# Compute sine and cosine values for each x
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y_cos, label='cos(x)', color='orange', linestyle='--')

# Add title and labels
plt.title('Graph of sin(x) and cos(x)')
plt.xlabel('x')
plt.ylabel('y')

# Add legend to distinguish the lines
plt.legend()

# Show the plot
plt.show()