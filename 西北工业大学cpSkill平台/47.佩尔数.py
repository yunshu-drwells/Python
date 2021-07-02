#迭代
n = int(input())
def Pell(n):
    pell = [i for i in range(n+1)]
    pell[0] = 0
    pell[1] = 1
    for i in range(2, n+1):
        pell[i] = 2*pell[i-1] + pell[i-2]
    return pell[n]
print(Pell(n))



#递归
n = int(input())
def pell(n):
    if 0 == n:
        return n
    if 1 == n:
        return n
    else:
        return 2*pell(n-1)+pell(n-2)
print(pell(n))
