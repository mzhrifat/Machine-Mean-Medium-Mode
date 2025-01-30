#Noraml data distribution
"""
import numpy
import matplotlib.pyplot as plt

x=numpy.random.normal(5.0,1.0,1000)

plt.hist(x,100)
plt.savefig('hist.png',format="png")

#plt.show()

# Generate random data with a normal distribution
import numpy as np
import matplotlib.pyplot as plt


mean = 5.0
std_dev = 1.0
data = np.random.normal(mean, std_dev, 100000)

# Plot histogram
plt.hist(data, bins=100, alpha=0.7, color='blue', edgecolor='black')
plt.title('Normal Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# Generate random data with a normal distribution
import numpy as np
mean=5.0
std_dev=1.0
data=np.random.normal(mean,std_dev,10000)

#calculated mean and medium

calculated_mean=np.mean(data)
calculated_median=np.median(data)


print(f"calculated Mean:{calculated_mean}")
print(f"calculated Median:{calculated_median}")
"""

# Generate random data with a normal distribution
import numpy as np
mean = 5.0
std_dev = 1.0
data = np.random.normal(mean, std_dev, 100000)

# Calculate percentiles
percentile_25 = np.percentile(data, 25)
percentile_50 = np.percentile(data, 50)
percentile_75 = np.percentile(data, 75)

print(f"25th Percentile: {percentile_25}")
print(f"50th Percentile (Median): {percentile_50}")
print(f"75th Percentile: {percentile_75}")

