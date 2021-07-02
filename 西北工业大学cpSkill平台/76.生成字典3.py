import copy
List = list(input().split())
List.reverse()
def recursion(dic, resDict, st):
    dic[st] = resDict
resDict = {}
dic = {}
for i in List:
    recursion(dic, resDict, i)
    resDict = copy.deepcopy(dic) #深拷贝
    dic = {}
print(resDict)



import copy
List = list(input().split())
List.reverse()
def recursion(resDict, dic, st):
    resDict[st] = dic
resDict = {}
dic = {}
for i in List:
    recursion(resDict, dic, i)
    dic = copy.deepcopy(resDict) #深拷贝
    resDict = {}
print(dic)

"""
1 2 3 4
"""
