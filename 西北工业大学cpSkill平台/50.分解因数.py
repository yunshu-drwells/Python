def dfs(a, m):
    if a == 1:
        return 1
    if m == 1:
        return 0
    if a % m == 0:
        return dfs(a,m-1) + dfs(a / m,m);  
    return dfs(a,m-1)
a = int(input())
print(dfs(a, a))
