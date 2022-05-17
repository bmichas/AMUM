import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
sc = ax.scatter([1,2,3,4], [1,2,4,5])

def asd(ew):
    print(sc.contains(ew))

fig.canvas.mpl_connect('motion_notify_event', asd)
plt.show()