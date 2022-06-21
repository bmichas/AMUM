import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

k = np.array([[-1,-1,1,1],[-1,1,1,-1]])

def animate(a):
    w = a/10
    opy = np.array([[1, w],
                [0,1]])
    kopy = opy @ k

    plt.clf()
    plt.xlim(-5,5)
    plt.ylim(-2,2)
    plt.fill(kopy[0,:],kopy[1,:])

fig, ax = plt.subplots(figsize=(6,6))



ani = matplotlib.animation.FuncAnimation(fig, animate, frames=40, interval=33, repeat=True) 
plt.show()