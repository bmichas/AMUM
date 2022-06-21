import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import mpl_toolkits.mplot3d.axes3d as p3

k = np.array([[-1,-1,-1,-1, 1, 1, 1, 1],
              [-1,-1, 1, 1,-1,-1, 1, 1],
              [-1, 1,-1, 1,-1, 1,-1, 1]])

def animate(a):
    deg = a*2
    rot = np.array([[np.cos(np.radians(deg)),-1*np.sin(np.radians(deg)),0],
                    [np.sin(np.radians(deg)),np.cos(np.radians(deg)),0 ],
                   [0,0,1]])
    ko = rot @ k
    plt.clf()
    ax = p3.Axes3D(fig)
    ax.set_ylim3d([-4,4])
    ax.set_zlim3d([-4,4])
    ax.set_xlim3d([-4,4])
    ax.scatter(ko[0,:], ko[1,:], ko[2,:])

fig = plt.figure()
ax = p3.Axes3D(fig)


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=33, repeat=True) 
plt.show()