##This is a code to find a peak with data which is created randomly.
##Writers; Luigi and Yildiz

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

##first we need to generate random data
data = np.random.randint(10, size=100)
print(data)
#np.shape(data)
y = data
x = np.linspace(0, 100, 100)
print(x)
np.shape(x)
plt.plot(x, y)

