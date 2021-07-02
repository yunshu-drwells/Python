chStr = input()
chLis = []
for i in range(len(chStr)):
    chLis.append(chStr[i])
n = int(input())
def f(n, Lis):
    dic = {}
    for i in range(0,26):
        dic[chr(i+ord('a'))] = chr(219-i-ord('a'))
    for i in range(n-1, len(Lis)):
        Lis[i] = dic[Lis[i]]
f(n, chLis)
print("".join(chLis))
"""
paradox
3
"""
