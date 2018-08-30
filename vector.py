import numpy as np

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self): #informal representation
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self): #formal representation
        return "{}{}".format(self.__class__.__name__, str(self)) #fetches own name, and __str__

    def __add__(self, other): #u.__add__(v) -> Vector3D.__add__(u, v)
        if isinstance(other, Vector3D): #if other is class Vector3D
            return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return self.__class__(self.x + other, self.y + other, self.z + other)
    #    else:
    #        raise TypeError("Cannot add vector and {}".format(type(other)))

    def __sub__(self, other): #u.__sub__(v) -> Vector3D.__sub__(u, v)
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)
        # return self + -other, fungerer gitt at neg er implementert

    def __neg__(self): #negate (invert)
        return self.__class__(-self.x, -self.y, -self.z)

'''
self.__class__ is implemented to prevent problems upon inheriteing, with different class names
'''


u = Vector3D(2,2,0)
v = Vector3D(1,0,1)

print(u+1)
