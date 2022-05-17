import matplotlib.pyplot as plt
import numpy as np
from pyparsing import alphas


def my_meshgrid(x,y):
    X = np.array([x]*len(y))
    Y = np.array([y]*len(x)).T
    return X, Y

def f(x,y): 
    return 0.5*np.sin(x**3) + 0.25*np.sin((y + np.pi)**2)


n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(-np.pi,np.pi/2,n)
X, Y = my_meshgrid(x,y)
Z = f(X,Y)

plt.contourf(X,Y,Z,cmap = 'jet', alpha = 0.75)
plt.contour(X,Y,Z, colors = 'black', linewidths = 1.2)
plt.show()