import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

k = np.array([[-1,-1,1,1],[-1,1,1,-1],[1,1,1,1]])

def animate(a):
    deg = a*2
    a= a/10
    rot = np.array([[np.cos(np.radians(deg)),-1*np.sin(np.radians(deg)),a],
                    [np.sin(np.radians(deg)),np.cos(np.radians(deg)),a ],
                   [0,0,1]])
    krot = rot @ k
    plt.clf()
    plt.xlim(-2,7)
    plt.ylim(-2,7)
    plt.fill(krot[0,:],krot[1,:])

fig, ax = plt.subplots(figsize=(6,6))



ani = matplotlib.animation.FuncAnimation(fig, animate, frames=40, interval=33, repeat=True) 
plt.show()