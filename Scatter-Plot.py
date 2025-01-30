"""
import numpy
import matplotlib.pyplot as plt

x=[4,6,8,10,12,14,16,18]
y=[22,24,28,30,12,14,40,12]

plt.scatter(x,y)

plt.show()
"""

import numpy
import matplotlib.pyplot as plt

x=numpy.random.normal(10.0,2.0,1000)
y=numpy.random.normal(5.0,1.0,1000)

plt.scatter(x,y)
plt.show()