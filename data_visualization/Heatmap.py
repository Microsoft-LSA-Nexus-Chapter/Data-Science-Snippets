import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
data = np.random.rand(10, 10)
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Heatmap')
plt.show()