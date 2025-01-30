
import matplotlib.pyplot as plt

from scipy import stats

x = [1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300]
y = [300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000, 460000, 480000]

slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
    return slope * x+ intercept

mymodel=list(map(myfunc,x))

plt.scatter(x,y)

plt.plot(x,mymodel)

plt.show()


print(f"coorelation coefficient (r):{r}")