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
            return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z) #returns _object_
        elif isinstance(other, (int, float)):
            return self.__class__(self.x + other, self.y + other, self.z + other)
    #    else:
    #        raise TypeError("Cannot add vector and {}".format(type(other)))

    def __sub__(self, other): #u.__sub__(v) -> Vector3D.__sub__(u, v)
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)
        # return self + -other, fungerer gitt at neg er implementert

    def __neg__(self): #negate (invert)
        return self.__class__(-self.x, -self.y, -self.z)

    def dot(self, other):
        if isinstance(other, self.__class__):
            return self.x*other.x + self.y*other.y + self.z*other.z
        elif isinstance(other, (int, float)):
            return self.__class__(self.x*other, self.y*other, self.z*other)

    def __mul__(self, other):
        return self.dot(other)

    def __rmul__(self, other): #right hand multiplication
        return self.dot(other)

    def cross(self, other):
        x = self.y*other.z - self.z*other.y
        y = self.z*other.x - self.x*other.z
        z = self.x*other.y - self.y*other.x
        return self.__class__(x, y, z)

    def __matmul__(self, other): #matrix multiplication
        return self.cross(other)

    def perpendicular(self, other):
        return np.isclose(self*other, 0)
        #return abs(self*other) < 1e-9

    @property
    def length(self):
        return np.sqrt(self*self)

    @length.setter
    def length(self, new_length):
        scale = new_length/self.length
        self.x *= scale
        self.y *= scale
        self.z *= scale

    def unit_vector(self): #return u_vector
        new_vector = self.__class__(self.x, self.y, self.z)
        new_vector.length = 1
        return(new_vector)
'''
self.__class__ is implemented to prevent problems upon inheriteing, with different class names
'''


u = Vector3D(2,2,0)
v = Vector3D(1,0,1)
w = u @ v
print(u+1)

print(3*u)

u.length = 2.5
print(u.length)
print(u)
print(u.unit_vector())

print(u == v) # __eq__ (equality)

### __getitem__, __setitem__ tillater indeksering av objektet ###
