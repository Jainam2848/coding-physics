import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt('http://www-personal.umich.edu/~mejn/cp/data/velocities.txt', float)

t = data[:, 0]
v = data[:, 1]
#x = sum(v*t)



#print(x)    
n = len(v)   #number of slices
b = 100      #upper limit
a = 0        #lower limit
h = (b-a)/n

s = []

for k in range(1,n):
    s+= v(a+h*k)*t(a+h*k)

print(h*s)
plt.plot(t,v)