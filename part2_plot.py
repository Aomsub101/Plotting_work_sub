import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
x, y = np.meshgrid(x , y)

def x_t_y():
    z = x * y

    ax.plot_surface(x, y, z, cmap='rainbow_r')
    ax.set_title('f(x, y) = x * y')
    plt.show()

def x_2_y_2():
    z = x**2 +  y**2

    ax.plot_surface(x, y, z, cmap='winter_r')
    ax.set_title('f(x, y) = x^2 + y^2')
    plt.show()

def sin_3x_y():
    z = np.sin(3*x) * y

    ax.plot_surface(x, y, z, cmap='PuRd_r')
    ax.set_title('f(x, y) = sin(3x) * y')
    plt.show()

# x_t_y()
x_2_y_2()
# sin_3x_y()
