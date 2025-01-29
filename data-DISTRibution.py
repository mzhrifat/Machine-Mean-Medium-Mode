#এলোমেলো ডেটাসেট তৈরি করা
#০ থেকে ৫ এর মধ্যে ২৫০টি এলোমেলো ভাসমান সংখ্যা তৈরি করুন:
"""
import numpy

x=numpy.random.uniform(0.0,5.0,20)

print(x)


#Draw a histogram:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 20)

plt.hist(x,5)
plt.title("Histogram of Random Data")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

"""

#Big Data Distribution

import numpy
import matplotlib.pyplot as plt

x=numpy.random.uniform(0.0,5.0,100000)

plt.hist(x,100)
plt.title("Histogram of Random Data")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()