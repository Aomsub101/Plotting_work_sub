import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 40)
x_square = x ** 2
plt.plot(x, x_square, label='f(x) = x^2', color='green', marker='*')

x_t_sin2x = x * np.sin(2*x)
plt.plot(x, x_t_sin2x, label='f(x) = x * sin(2x)', color='red', linestyle='--', marker='1')

arctg = np.arctan(x)
plt.plot(x, arctg, label='f(x) = arctan(x)', color='blue', linestyle=':', marker='4')

plt.xlabel('x')
plt.ylabel('y')
plt.title('All plots')
plt.legend()
plt.grid(True)
plt.show()

