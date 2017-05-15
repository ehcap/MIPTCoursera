import math
import matplotlib.pyplot as pl
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import differential_evolution

def func1(x):
    return 3*x**4-8*x**3+6*x**2-12
x0 = range(-3,4, 1)
y =  np.array()
[func1(z) for z in x0]
pl.plot(x0, y)
pl.show()
res2 =  minimize(func1, -2., method='BFGS', tol=1e-6)
print res2

def func(x):
    import numpy
    return math.sin(x/5.) * math.exp(x/10.) + 5 * math.exp(-x/2.)

def absfunc(x):
    return int(func(x))

x = np.arange(1, 50.5, 0.5)
x0 = range(1,30, 1)
y =  np.array([func(z) for z in x])
absy  = np.array([absfunc(z) for z in x])

print absy

#line = pl.plot(x,y)
pl.plot(x,absy)
#pl.setp(line, color='r', linewidth=2.0)
pl.show()

res2 =  minimize(func, 2., method='BFGS', tol=1e-6)
#print res2
res30 =  minimize(func, 30., method='BFGS', tol=1e-6)
#print res30

#print res2.fun , ' ', res30.fun

bounds = [(1,30)]
res3 = differential_evolution(func, bounds)

#print res3


res30 =  minimize(absfunc, 30., method='BFGS', tol=1e-6)
print res30
bounds = [(1,30)]
res3 = differential_evolution(absfunc, bounds)
print res3

