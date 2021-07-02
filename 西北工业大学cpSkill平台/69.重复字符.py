st = str(input())
charSet = {}
for i in st:
    if i in charSet:
        charSet[str(i)] += 1 
    else:
        charSet[str(i)] = 1
# 清洗字符只出现一次的数据
keys = charSet.keys()
resultSet = {}
for it in keys:
    if charSet[it] >= 2:
        resultSet[it] = charSet[it]
#打印
keys = resultSet.keys()
for it in keys:
    print(it,resultSet[it], sep = " ")
"""
googleapplemicrosoft
charSet[str(i)]+int(1)
"""
