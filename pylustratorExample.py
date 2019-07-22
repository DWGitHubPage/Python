# Python3.7.4

import matplotlib.pyplot as plt
import numpy as np
import pylustrator

pylustrator.start()

np.random.seed(1)
t = np.arange(0.0, 10, 0.10)
y = 100 * np.sin(np.pi * t)
a, b = np.random.normal(loc=(2., 1.), scale=(10., 4.), size=(100, 2)).T
b += a

plt.figure(1)
plt.subplot(131)
plt.plot(t, y, color="orange")

plt.subplot(132)
plt.plot(a, b, "o", color="grey")

plt.subplot(133)
plt.bar(0, np.mean(a), color="black")
plt.bar(1, np.mean(b), color="red")


plt.show()
