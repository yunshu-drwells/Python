#借助zip函数将键值对打包成元组生成列表来创建字典
keysList = input().split()
valuesList = input().split()
resultDict = dict(zip(keysList, valuesList))
print(resultDict)



#直接遍历两个分别代表键值列表创建字典
list1 = list(map(str, input().split()))
list2 = list(map(str, input().split()))
resDict = {}
for i in range(len(list1)):
    resDict[list1[i]] = list2[i]
print(resDict)

"""
a b c d e
5 4 3 2 1
"""
