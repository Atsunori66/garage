import numpy as np
import matplotlib.pyplot as plt

xplot = []
yplot = []

n = 10000

for x in range(n):
    xplot.append(x)

    y = (1 - 1 / n) ** n
    yplot.append(y)

plt.plot(xplot, yplot)
plt.show()

#print(y)