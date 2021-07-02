L1 = input().split()
L2 = input().split()
s1 = set(L1)
s2 = set(L2)
res = s1.symmetric_difference(s2) 
res = list(res)
res.sort(key=str)
print(" ".join(res))
"""
symmetric_difference_update() 方法
移除当前集合中在另外一个指定集合相同的元素，
并将另外一个指定集合中不同的元素插入到当前集合中。
"""







list1 = list(map(str, input().split(" ")))
list2 = list(map(str, input().split(" ")))
dict1 = {}
dict2 = {}
#列表转换为字典
for i in list1:
    dict1.setdefault(i)
for i in list2:
    dict2.setdefault(i)
#将差异元素放入dict3
dict3 = {}
keys1 = dict1.keys()
for it in keys1:
    if it in dict2:
        continue
    else:
        dict3.setdefault(it)
keys2 = dict2.keys()
for it in keys2:
    if it in dict1:
        continue
    else:
        dict3.setdefault(it)
#结果字典转换为列表排序，然后转为字符串输出
res = list(dict3.keys())
res.sort(key = str)
print(" ".join(res))
## 这道题和列表差异如出一辙，直接使用之前的代码并且对最后的结果列表排序

"""
green blue
blue yellow
"""
