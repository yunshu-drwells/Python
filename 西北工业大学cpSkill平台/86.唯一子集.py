#孙豪
from math import pow
class A:
    def __init__(self, _s):
        self.s = _s

    def fun(self):
        Len = len(self.s)
        ll = []
        for ii in range(0, int(pow(Len, 2) - 1)):
            lll = []
            for j in range(Len):
                if (ii >> j) % 2:
                    lll.append(self.s[Len - j - 1])
            lll.sort()
            ll.append(lll)
        if ll[-1] != self.s:
            ll.append(self.s)
        return ll


x = input()
l1 = x.split()
for i in range(0, len(l1)):  # 变为int
    l1[i] = int(l1[i])

s1 = set(l1)
l1 = list(s1)  # 去重
l1.sort(reverse=False)  # 排序
a = A(l1)
print(a.fun())

"""
6 5 4
"""



class SubSet:
    def __init__(self, Lis):
        self._Lis = Lis
    def sub(self):
        subS = [[]]
        subs = []
        for i in range(len(self._Lis), 0, -1):
            for j in range(i, len(self._Lis)+1):
                subs.clear()
                if len(self._Lis) -1-j == 0:
                    subs.append[j]
                    subS.append(subs)
                else:
                    print()

L = list(map(int, input().split()))
subSet = SubSet()
print(subSet.sub())
