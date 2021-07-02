#使用difference函数
set1 = set(input().split())
set2 = set(input().split())
resList = list(set1.difference(set2))
resList.sort(key = str)
print(" ".join(resList))



list1 = list(map(str, input().split(" ")))
list2 = list(map(str, input().split(" ")))
dict1 = {}
dict2 = {}
#列表转换为字典
for i in list1:
    dict1.setdefault(i)
for i in list2:
    dict2.setdefault(i)
#将存在第一个集合且不存在第二个集合的元素放入dict3
dict3 = {}
keys1 = dict1.keys()
for it in keys1:
    if it in dict2:
        continue
    else:
        dict3.setdefault(it)
#结果字典转换为列表排序，然后转为字符串输出
res = list(dict3.keys())
res.sort(key = str)
print(" ".join(res))

"""
green blue
blue yellow
"""
