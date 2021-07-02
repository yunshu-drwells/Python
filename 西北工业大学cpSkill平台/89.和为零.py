class ChooseThree:
    def __init__(self, lis):
        self._Lis = lis
    def chooses(self):
        Res = []
        for i in range(len(self._Lis)):
            for j in range(i+1, len(self._Lis)):
                for k in range(j+1, len(self._Lis)):
                    if 0 == self._Lis[i]+self._Lis[j]+self._Lis[k]:
                        subRes = []
                        subRes.append(self._Lis[i])
                        subRes.append(self._Lis[j])
                        subRes.append(self._Lis[k])
                        Res.append(subRes)
                    else:
                        continue
        return Res
lis = list(map(int, input().split()))
st = ChooseThree(lis)
print(st.chooses())

"""
-25 -12 -7 -3 15 4 8 10
"""
