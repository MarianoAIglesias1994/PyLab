#C:\>py -m pip install numpy
#C:\>py -m pip install matplot.lib

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(1024)
a = np.zeros(256)
s = np.ones(512)
d = np.append(a,s)
d = np.append(d,a)

b = np.fft.fft(d)

plt.plot(t, abs(b))
plt.show()
