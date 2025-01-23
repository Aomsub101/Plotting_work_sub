import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
x_square = x ** 2
plt.plot(x, x_square, label='x_square', color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title('All plots')
plt.legend()
plt.grid(True)
plt.show()

