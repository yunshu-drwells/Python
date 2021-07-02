list1 = list(map(str, input().split(" ")))
list2 = list(map(str, input().split(" ")))
dict1 = {}
dict2 = {}
for i in list1:
    dict1.setdefault(i)
for i in list2:
    dict2.setdefault(i)
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
print(" ".join(list(dict3.keys())))
"""
1 3 4 7 9
1 2 4 6 7 8
"""
