
"""
import numpy

from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel=numpy.poly1d(numpy.polyfit(x,y,3))

print(r2_score(y,mymodel(x)))



#Predict Future Values

#import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score


x=[1,2,3,6,7,8,9]
y=[50,100,70,80,90,60,80]

mymodel=numpy.poly1d(numpy.polyfit(x,y,3))

speed=mymodel(7)
print(speed)
#plt.scatter(x,y)
#plt.plot(mymodel)
#plt.show()





#Bad fit

import numpy
import matplotlib.pyplot as plt

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel=numpy.poly1d(numpy.polyfit(x,y,3))

myline=numpy.linspace(2,95,100)

plt.scatter(x,y)
plt.plot(myline,mymodel(myline))

plt.show()
"""

import numpy
from sklearn.metrics import r2_score

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))