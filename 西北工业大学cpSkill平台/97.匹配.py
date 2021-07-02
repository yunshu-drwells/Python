#用求交集的方式求
str1, str2 = map(str, input().split(" "))
dic1 = {}
dic2 = {}
res = []
for i in range(len(str1)):
    dic1.setdefault(str1[i])
for i in range(len(str2)):
    dic2.setdefault(str2[i])
keys = dic1
for it in keys:
    if it in dic2:
        res.append(it)
print(len(res))


"""
abcdef defghia
"""
