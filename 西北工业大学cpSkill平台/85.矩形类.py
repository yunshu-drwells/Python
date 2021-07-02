class Rectangle:
    def __init__(self, L, W):
        self._L = L
        self._W = W
    def perimeter(self):
        return self._L*self._W
l,w = map(int, input().split())
r = Rectangle(l, w)
print(r.perimeter())

"""
5 6
"""
