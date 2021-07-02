str1 = list(input().split(","))
str2 = list(input().split(","))
str1 += str2
resDict = {}
for st in str1:
    key_value = st.split(":")
    if key_value[0] in resDict:
        resDict[key_value[0]] += int(key_value[1])
    else:
        resDict[key_value[0]] = int(key_value[1])
print(resDict)
"""
a:100,b:200,c:300
a:300,b:200,d:400
"""
