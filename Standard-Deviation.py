#NumPy দিয়ে স্ট্যান্ডার্ড ডেভিয়েশন (ভ্যারিয়েন্সের বর্গমূল)বের করা
"""
import numpy

speed = [32, 111, 138, 28, 59, 77, 97]
x=numpy.std(speed)
print(x)
"""

#NumPy দিয়ে ভ্যারিয়েন্স বের করা:

import numpy

speed = [32, 111, 138, 28, 59, 77, 97]

x=numpy.var(speed)
print(x)

import numpy

speed = [32, 111, 138, 28, 59, 77, 97]

x = numpy.std(speed)

print(x)