import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def prob(p):
    r = random.random()
    return p > r

def genData(length, y0=1000, vola=0.1, statisize=1,
            linearadd=1, expoadd=0.01, flashreduce=0.1,
            dynamicflashchance=0.000001, flashchance=0.00001,
            dynamic_flash_crash=True):
    arr = []
    for _ in range(length):
        # Statistic movements:
        r = np.random.normal(loc=0, scale=y0*vola)
        
        if y0 > 0:
            y0 += statisize*r

            # Linear movement:
            if prob(0.5):
                y0 += linearadd

            # Exponential movement:
            if prob(0.06):
                y0 *= 1 + expoadd

            # Flash crash:
            if dynamic_flash_crash:
                if prob(dynamicflashchance*y0):
                    y0 *= flashreduce
            else:
                if prob(flashchance):
                    y0 *= flashreduce
        else:
            y0 = 0

        arr.append(y0)
    return arr

x = genData(length=2000)


plt.plot(x)
plt.show()

