x = input()
L = x.split(";")
result = []
for i in range(0, len(L)):
    s = str(L[i])
    s = s.strip("(")
    s = s.strip(")")
    m, n = map(int, s.split(","))
    t = (m, n)
    result.append(t)
print(sorted(result, key=lambda x: (x[1])))

"""
(1,105);(2,102);(3,104);(4,103);(5,101)
"""
