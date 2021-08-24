import random
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

x = np.linspace(0, 10, 1000)
x1 = [0] * 50
y1 = [0] * 50
x2 = [0] * 50
y2 = [0] * 50
ycorrecta = 50

for i in range(50):
    x1[i] = random.randint(0, 4)
    y1[i] = random.randint(0, 4)
    x2[i] = random.randint(5, 10)
    y2[i] = random.randint(5, 10)

plt.plot(x1, y1, 'o', color='black')
plt.plot(x2, y2, 's', color='red')
plt.plot(x, -x+9, color="red")
plt.plot(x, x)
plt.show()