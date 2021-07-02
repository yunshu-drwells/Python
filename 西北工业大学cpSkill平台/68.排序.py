x = input()
L = x.split(" ")
resultL = sorted(L, key=lambda x: int(x)*-1)
s = " ".join(resultL)
print(s)

"""
-1 -67 92 36 99 44 66 -55 2 0 12 10
"""
