import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 40)
x_square = x ** 2
plt.plot(x, x_square, label='x_square', color='green', marker='*')

x_t_sin2x = x * np.sin(2*x)
plt.plot(x, x_t_sin2x, label='x * sin(2*x)', color='red', linestyle='--', marker='1')

arctg = np.arctan(x)
plt.plot(x, arctg, label='arctg', color='blue', linestyle=':', marker='4')

plt.xlabel('x')
plt.ylabel('y')
plt.title('All plots')
plt.legend()
plt.grid(True)
plt.show()

