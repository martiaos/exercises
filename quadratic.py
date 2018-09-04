import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.scimath import sqrt #Import sqrt-function allowing negative

class Quadratic: #def class
    def __init__(self, a2, a1, a0):
        self.a2 = a2 #get coefficients
        self.a1 = a1
        self.a0 = a0

    def __call__(self, x): #call function evaluates the polynomial
        return self.a2*x**2 + self.a1*x + self.a0

    def __str__(self): #returns a pretty print of functional form
        return("%gx^2 + %gx + %g" %(self.a2, self.a1, self.a0))

    def __add__(self, other): #adds two polynomials, returns new object
        return Quadratic(self.a2 + other.a2,
                         self.a1 + other.a1,
                         self.a0 + other.a0)

    def roots(self): #calculate roots
        a = self.a2
        b = self.a1
        c = self.a0
        if (b**2 - 4*a*c) < 0: #if imaginary
            return None #drop
        else:
            x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
            x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
        if x1 == x2: #if equal
            return x1 #return one
        else:
            return x1, x2

    def intersect(self, other):
        t = [i for i in range (-1000, 1000, 2000)]
        intersect = []
        for n in t:
            if np.isclose(self(n), other(n)):
                intersect.append(n)
        return intersect

f  = Quadratic(2, -4, 4)
g = Quadratic(-2, 4, -4)

h = f + g
print(h)

x = np.linspace(-5, 5, 101)
plt.plot(x, h(x))
plt.show()

d = Quadratic(2, -2, 2)
e = Quadratic(1, -2, 1)
i = Quadratic(1, -3, 2)

print(d.roots())
print(e.roots())
print(i.roots())
print(f.intersect(g))
