x = input()
L = x.split(",")
resultL = sorted(L, key=lambda x: (int(x[1:len(x)])))
s = " ".join(resultL)
print(s)
"""
a1,a22,a3,a8,a10,a100
"""
