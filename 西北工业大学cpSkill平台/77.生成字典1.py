n = int(input())
List = []
for i in range(1, n+1):
    List.append(i)
resDict = {}
for i in List:
    resDict[i] = i*i
print(resDict)

"""
4
"""
