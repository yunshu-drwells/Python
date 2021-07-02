keys = input().split(" ")
values = input().split(" ")   
getDict = dict(zip(keys, values))
Lis = dict(sorted(getDict.items(), key=lambda getDict:getDict[1],reverse = False))
#sorted函数返回的是列表元素所排序的迭代对象的元素
print(" ".join(Lis.keys()))

"""
a b c d e f g h i
0 1 1 0 1 2 2 0 1
"""
