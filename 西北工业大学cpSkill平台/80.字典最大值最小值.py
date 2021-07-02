str1 = list(input().split(","))
getDict = {}
for st in str1:
    key_value = st.split(":")
    if key_value[0] in getDict:
        continue
    else:
        getDict[key_value[0]] = int(key_value[1])
#按值排序
resDict = dict(sorted(getDict.items(), key=lambda getDict:getDict[1],reverse = False))
values = list(resDict.values())
print(values[len(values)-1], values[0])

"""
a:500,b:5874,c:560
"""
