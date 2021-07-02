class Calculate:
    def __init__(self, x, n):
        self._x = x
        self._n = n
    def pow(self):
        res = 1
        if n < 0:
            self._x = 1/self._x
        for i in range(0, abs(n)):
            res *= self._x
        return res
x, n = map(int, input().split())
c = Calculate(x, n)
print(c.pow())
"""
2 -3
"""
