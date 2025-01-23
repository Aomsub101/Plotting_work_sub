import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('csv_data/points.csv', delimiter=',')
distances = np.loadtxt('csv_data/distances.csv')


plt.scatter(points[:,0],points[:,1], c=distances, cmap='winter')
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='distance')
plt.show()

