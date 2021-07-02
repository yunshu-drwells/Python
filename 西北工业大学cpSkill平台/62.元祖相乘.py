m = map(int, input().split(" "))
map2tup = tuple(m)
result = 1
for i in range(len(map2tup)):
    result *= map2tup[i]
print(result)

"""
1 2 -3 -4 5 6 -7
"""
