import numpy as np
import matplotlib.pyplot as plt

hist_values = np.loadtxt('../csv_data/values_for_hist.csv')

plt.hist(hist_values, bins=30, edgecolor='black', color='red')
plt.title('Histogram plot')
plt.xlabel('Value')
plt.ylabel('Count occurence of value')
plt.show()
