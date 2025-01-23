import numpy as np
import matplotlib.pyplot as plt

bar_values = np.loadtxt('../csv_data/values_for_bars.csv')

unique, counts = np.unique(bar_values, return_counts=True)

plt.bar(unique, counts)
plt.xlabel('Number')
plt.ylabel('Number counts')
plt.title('Count occurence of each number')
plt.show()
