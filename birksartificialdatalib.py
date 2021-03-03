import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def prob(p):
    r = random.random()
    return p > r

def genData(length, y0=1000, vola=10):
    arr = []
    for _ in range(length):
        # Statistic movements:
        r = np.random.normal(loc=0, scale=vola)
        s = 1
        y0 += s*r

        # Linear movement:
        a = 1
        if prob(0):
            y0 += a

        # Exponential movement:
        ap = 0.1
        bp = 0.0015
        if prob(0.6):
            y0 += a*np.exp(np.abs(bp*y0))
        
        # Flash crash:
        fl = 0.1
        if prob(0.00001*y0):
            y0 *= fl

        arr.append(y0)
    return arr

x = genData(length=2000)


plt.plot(x)
plt.show()

