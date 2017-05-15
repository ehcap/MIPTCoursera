import math
import numpy as np
def func(x):
    return math.sin(x/5.) * math.exp(x / 10.) + 5 * math.exp(-x/2.)
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

# 1 task
a1 = np.array([[1.,1.],[1., 15.]])
f1 = np.array([[func(1)],[func(15)]])
print a1
print a1.shape
print f1 , f1.shape

x1 = np.linalg.solve(a1, f1)
print x1
print  a1.dot(x1)

# 2 task
a2 = np.array([[1.,1.,1],[1.,8., 8.**2],[1., 15., 15.**2]])
f2 = np.array([[func(1)],[func(8)],[func(15)]])
print a2
print a2.shape
print f2 , f2.shape

x2 = np.linalg.solve(a2, f2)
print x2
print  a2.dot(x2)


# 3 task
a3 = np.array([[1.,1.,1.,1.],[1.,4.,4.**2, 4.**3],[1., 10., 10.**2, 10.**3],[1., 15., 15.**2, 15.**3]])
f3 = np.array([[func(1)],[func(4)],[func(10)],[func(15)]])
print a3
print a3.shape
print f3 , f3.shape

x3 = np.linalg.solve(a3, f3)
print x3
print  a3.dot(x3)

a3 = np.array([[1.,1.,1.,1.,1],[1.,3.,3.**2, 3.**3, 3**4],
               [1., 9., 9.**2, 9.**3, 9**4],
               [1., 12., 12.**2, 12.**3, 12**4],
               [1., 15., 15.**2, 15.**3, 15**4]])
f3 = np.array([[func(1)],[func(3)],[func(9)],[func(12)],[func(15)]])
x3 = np.linalg.solve(a3, f3)
print x3
