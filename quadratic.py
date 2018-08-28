import matplotlib.pyplot as plt
import numpy as np

class Quadratic:
    def __init__(self, a0, a1, a2):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2

    def __call__(self, x):
        return self.a0 + self.a1*x + self.a2*x**2

    def __str__(self):
        return("%g + %gx + %gx^2" %(self.a0, self.a1, self.a2))

f  = Quadratic(1, -2, 1)
x = np.linspace(-5,5,101)
plt.plot(x, f(x))
plt.show()
print(f)
