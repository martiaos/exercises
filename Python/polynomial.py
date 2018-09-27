import matplotlib.pyplot as plt
import numpy as np

class Polynomial():
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __call__(self, x):
        sum = 0
        for key in self.coeffs:
            sum += (x**key)*self.coeffs[key]
        return sum

    def __str__(self):
        poly_list = ''
        for key, value in sorted(self.coeffs.items()):
            poly_list += '%g*x^%g +' %(value, key)
        return poly_list[:-1]

    def __add__(self, other):
        other_coeffs = other.coeffs
        coeffs = self.coeffs
        for other_key in other_coeffs:
            if other_key in coeffs:
                coeffs[other_key] += other_coeffs[other_key]
            else:
                coeffs[other_key] = other_coeffs[other_key]
        return Polynomial(coeffs)

coeffs = {0:1, 5:-1, 10:1}
f = Polynomial(coeffs)

print(f)

x = np.linspace(-1, 1, 101)
plt.plot(x, f(x))
plt.show()

f = Polynomial({0:1, 5:-7, 10:1})
g = Polynomial({5:7, 10:1, 15:-3})

print(f+g)
