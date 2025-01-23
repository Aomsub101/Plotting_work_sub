import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
x, y = np.meshgrid(x , y)

def x_t_y():
    z = x * y

    ax.plot_surface(x, y, z)
    ax.set_title('f(x, y) = x * y')
    plt.show()

def x_2_y_2():
    z = x**2 +  y**2

    ax.plot_surface(x, y, z)
    ax.set_title('f(x, y) = x * y')
    plt.show()

def sin_3x_y():
    z = np.sin(3*x) * y

    ax.plot_surface(x, y, z)
    ax.set_title('f(x, y) = x * y')
    plt.show()

# x_t_y()
# x_2_y_2()
sin_3x_y()
