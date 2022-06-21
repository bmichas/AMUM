import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import mpl_toolkits.mplot3d.axes3d as p3

k = np.array([[-1,-1,-1,-1, 1, 1, 1, 1],
              [-1,-1, 1, 1,-1,-1, 1, 1],
              [-1, 1,-1, 1,-1, 1,-1, 1]])


def animate(a):
    deg = a*5
    rot = np.array([[np.cos(np.radians(deg)),-1*np.sin(np.radians(deg)),0],
                    [np.sin(np.radians(deg)),np.cos(np.radians(deg)),0 ],
                   [0,0,1]])
    ko = rot @ k
    rot = np.array([[1,0,0],
                    [0,np.cos(np.radians(deg/2)),-1*np.sin(np.radians(deg/2))],
                    [0,np.sin(np.radians(deg/2)),np.cos(np.radians(deg/2))]])
    ko = rot @ ko
    
    plt.clf()
    ax = p3.Axes3D(fig)
    ax.set_ylim3d([-4,4])
    ax.set_zlim3d([-4,4])
    ax.set_xlim3d([-4,4])

    for p in range(k.shape[1]):
        for b in range(k.shape[1]):
            if np.linalg.norm(k[:,p] - k[:,b]) == 2:
                ax.plot(ko[0,[p,b]], ko[1,[p,b]], ko[2,[p,b]], c='b')

    
fig = plt.figure()
ax = p3.Axes3D(fig)


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=33, repeat=True) 
plt.show()