class SpecialGoals:
    def __init__(self, lis, n):
        self._Lis = lis
        self._n = n
    def find(self):
        res = ['', '+', '', '=', '']
        res[len(res)-1] = str(self._n)
        for i in range(len(self._Lis)):
            for j in range(i+1, len(self._Lis)):
                if self._Lis[i]+self._Lis[j] == self._n:
                    res[0] = str(self._Lis[i])
                    res[2] = str(self._Lis[j])
                    return " ".join(res)
lis = list(map(int, input().split()))
n = int(input())
sg = SpecialGoals(lis, n)
print(sg.find())

"""
1 2 1 4 5 6 7
5
"""
