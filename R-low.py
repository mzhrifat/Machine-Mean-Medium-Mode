#Bad data fit
"""
import matplotlib.pyplot as plt
import numpy

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel=numpy.poly1d(numpy.polyfit(x,y,3))

myline=numpy.linspace(2,95,100)

plt.scatter(x,y,color='red',label='Original Data',)
plt.plot(myline,mymodel(myline),color='blue',label='Fitted Model')


plt.xlabel('Hello')
plt.ylabel('World')

plt.title('Polynomial Regress with bad Fit')
plt.legend()
plt.show()
"""

#a shop sells prediction

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [50, 55, 57, 60, 65, 70, 80, 85, 90, 100]

mymodel=np.poly1d(np.polyfit(x,y,3))


new_days=np.linspace(1,15,100)
predicted_sales=mymodel(new_days)

plt.scatter(x, y, color='red', label='Actual Sales')
plt.plot(new_days, predicted_sales, color='blue', label='Fitted Model')
plt.xlabel('Days')
plt.ylabel('Sales (in units)')
plt.title('Sales Prediction Using Polynomial Regression')
plt.legend()
plt.show()