keys = []
values = []
while True:
    st = input()
    if st == "":
        break
    st = st.split(" ")
    keys.append(st[0])
    values.append(st[1])    
getDict = dict(zip(keys, values))

#按值排序
##print(sorted(getDict.items(), key = lambda kv:(int(kv[1]), kv[0])))
print(list(sorted(getDict.items(), key=lambda getDict:getDict[1],reverse = False)))
#按键排序
##print(sorted (getDict))
print(list(sorted(getDict.items(), key=lambda getDict:getDict[0],reverse = True)))
"""
语文 89
数学 91
英语 93
生物 77
地理 86
历史 85


"""








#键值排序示例：
d={"ok":1,"no":2}
#对字典按键排序，用元组列表的形式返回
d1 = sorted(d.items(), key=lambda d:d[0],reverse = False) #[('no', 2), ('ok', 1)]
print(d1)
#对字典按值排序，用元组列表的形式返回
d2 = sorted(d.items(), key=lambda d:d[1],reverse = True) #[('ok', 1), ('no', 2)]
print(d2)
