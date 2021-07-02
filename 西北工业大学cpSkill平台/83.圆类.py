class Circle:
    def __init__(self, x):
        self._r = r
    def area(self):
        return self._r*self._r*3.14
    def perimeter(self):
        return 2*self._r*3.14
r = float(input())
c = Circle(r)
print(c.area(), c.perimeter())

"""
8.0
"""
