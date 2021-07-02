M, N = map(int, input().split())
def Divide(m, n):
    if 0 == m or 1 == n:
       return 1
    elif n <= m:
        return Divide(m, n-1) + Divide(m-n, n)
    else:
        return Divide(m, m)
print(Divide(M, N))
