import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

k = np.array([[-1,-1,1,1],[-1,1,1,-1]])

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)


def animate(deg):
    deg = deg
    rot = np.array([[np.cos(np.radians(deg)),-1*np.sin(np.radians(deg))],
                    [np.sin(np.radians(deg)),np.cos(np.radians(deg)) ]])
    krot = rot @ k
    plt.clf()
    plt.fill(krot[0,:],krot[1,:])  
  
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=90, interval=33, repeat=True) 
plt.show()