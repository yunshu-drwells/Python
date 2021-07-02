n = int(input())
lis = []
for i in range(n):
    line = input().split()
    lis.extend(line)
res = []
for i in range(n): 
    if 0 == i:
        for j in range(n):
            res.append(lis[j])
    elif n-1 == i:
        for j in range(n*(n-1), n*n):
            res.append(lis[j])
    else:
        res.append(lis[(i+1)*(n-1)])
print(" ".join(res))
"""
3
1 2 3
4 5 6
7 8 9

4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""
