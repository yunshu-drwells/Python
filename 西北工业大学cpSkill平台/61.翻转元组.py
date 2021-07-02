import math
map = map(int, input().split(" "))
map2List = list(map)
r = len(map2List)>>1
r += len(map2List) % 2
for i in range(r):
    map2List[i] += map2List[-i-1]
    map2List[-i-1] = map2List[i]
tup = tuple(map2List)
print(tup)
