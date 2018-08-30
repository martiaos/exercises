import matplotlib.pyplot as plt
import numpy as np

class Quadratic:
    def __init__(self, a2, a1, a0):
        self.a2 = a2
        self.a1 = a1
        self.a0 = a0

    def __call__(self, x):
        return self.a2*x**2 + self.a1*x + self.a0

    def __str__(self):
        return("%gx^2 + %gx + %g" %(self.a2, self.a1, self.a0))

    def __add__(self, other):
        return Quadratic(self.a2 + other.a2,
                         self.a1 + other.a1,
                         self.a0 + other.a0)

    def roots(self):
        a1 = self.a1
        a2 = self.a2
        a3 = self.a3


f  = Quadratic(1, -2, 1)
g = Quadratic(-1, 6, -3)

h = f + g
print(h)

x = np.linspace(-5, 5, 101)
plt.plot(x, h(x))
plt.show()
