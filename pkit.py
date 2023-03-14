import numpy
import matplotlib.pyplot as plt
import random as r
x= numpy.random.uniform(0.0,5.0,1000)

plt.hist(x,150)
plt.show()
#plt.plot(list(r.randint(0,10000) for i in range(1000)),list(r.randint(0,10000) for i in range(1000)))
plt.hist(numpy.random.normal(5.0,1.0,1000),1000)
plt.show()