import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import mpl_toolkits.mplot3d.axes3d as p3


def f(x, y, t):
    return 0.5*np.sin(x**3) + 0.25*np.sin((y - t)**2)


def animate(i):
    X, Y = np.meshgrid(x, y)
    z = np.array(f(np.ravel(X), np.ravel(Y), i/10))
    Z = z.reshape(X.shape)
    plt.clf()
    ax = p3.Axes3D(fig)
    ax.plot_surface(X, Y, Z, cmap="gist_ncar")


n = 100
x = np.linspace(-np.pi/2, np.pi/2, n)
y = np.linspace(-np.pi, np.pi/2, n)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = p3.Axes3D(fig)
ax.set_xlim3d([-np.pi/2, np.pi/2])
ax.set_ylim3d([-np.pi, np.pi/2])

ani = matplotlib.animation.FuncAnimation(
    fig, animate, frames=80, interval=100, repeat=False)
plt.show()
