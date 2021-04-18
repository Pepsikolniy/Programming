import math
from enum import Enum

def equal(a, b, e=1E-10):
    if -e < a - b < e: return True
    else: return False

class coord_system(Enum):
      Cartesian = 0
      Polar = 1

class Point:
    def __init__(self, a1 = 0, a2 = 0, coord_system = coord_system.Cartesian):
        if (type(a1) == str):
            self.x = float( a1[1 : a1.find(',')].strip())
            self.y = float( a1[a1.find(',')+1: -2].strip())
        else:
            if (coord_system == coord_system.Cartesian):
                self.y = a2
                self.x = a1
            else:
                self.x = math.cos(a2) * a1
                self.y = math.sin(a2) * a1


    def __ne__(self, other):
        return True if not self == other else False

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def __str__(self):
      return f'({self.x},{self.y})'
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_r(self):
        return math.hypot(self.x, self.y)

    def get_phi(self):
        return math.atan2(self.y, self.x)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_r(self, r):
        self.x = math.cos(self.get_phi()) * r
        self.y = math.sin(self.get_phi()) * r

    def set_phi(self, phi):
        self.x = math.cos(phi) * self.get_r()
        self.y = math.sin(phi) * self.get_r()

    def __eq__(self, other):
        if type(other) != Point: return False
        return True if (abs(self.x - other.x) < 10**-10) and (abs(self.y - other.y) < 10**-10) else False

class Vector:
    def __init__(self, begin = None, end = None):
        if begin == None and end == None:
            self.point = Point(1,0)
        elif begin == None and end != None:
            self.point = end
        elif end == None and begin != None:
            self.point = begin
        else:
            self.point = Point(end.get_x() - begin.get_x(), end.get_y() - begin.get_y())

    def __eq__(self, other):
        return  self.point.x == other.point.x and self.point.y == other.point.y

    def __neg__(self):
        inverted = Point()
        inverted.set_x(-self.point.get_x())
        inverted.set_y(-self.point.get_y())
        return Vector(inverted)

    def __add__(self, other):
        summ = Point()
        summ.set_x(self.point.get_x() + other.point.get_x())
        summ.set_y(self.point.get_y() + other.point.get_y())
        return Vector(summ)

    def __sub__(self, other):
        sub = Point()
        sub.set_x(self.point.get_x() - other.point.get_x())
        sub.set_y(self.point.get_y() - other.point.get_y())
        return Vector(sub)

    def length(self):
        return self.point.get_r()

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            mul = Point()
            mul.set_x(self.point.get_x() * other)
            mul.set_y(self.point.get_y() * other)
            return Vector(mul)
        else:
            return self.length() * other.length() * math.cos(self.point.get_phi() - other.point.get_phi())


a = Vector(Point(1, 2))
b = Vector(Point(-2, 0), Point(-1, 2))
if a == b and b == a: print('Equality test passed')
else: print('Equality test failed')

na  = Vector(Point(-1, -2))
ox  = Vector(Point( 1,  0))
nox = Vector(Point(-1,  0))
oy  = Vector(Point( 0,  1))
noy = Vector(Point( 0, -1))
if a == -na and na == -a and -ox == nox and -oy == noy: print('Invert test passed')
else: print('Invert test failed')

if ox + oy + oy == a and -ox == -a + oy + oy: print('Summation test passed')
else: print('Summation test failed')

if -ox + oy == oy - ox and -oy + ox == ox - oy: print('Subtraction test passed')
else: print('Subtraction test failed')

if (ox * 3 == ox + ox + ox and
    oy * 3 == oy + oy + oy and
    ox * (-3) == -ox - ox - ox and
    oy * (-3) == -oy - oy - oy): print('Multiplication by number test passed')
else: print('Multiplication by number test failed')

if (equal(ox.length(), 1) and
    equal(oy.length(), 1) and
    equal((ox * 3 + oy * 4).length(), 5)): print('Length test passed')
else: print('Length test failed')

if (equal(ox*ox, ox.length()**2) and
    equal(oy*oy, oy.length()**2) and
    equal((ox*3 + oy*4)*(ox*3 + oy*4), (ox*3 + oy*4).length()**2)): print('Multiplication by Vector test passed')
else: print('Multiplication by Vector test failed')
