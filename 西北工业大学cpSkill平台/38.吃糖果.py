##迭代优化
def F(N):
    a = 1
    b = 2
    if N == 1 or N == 2:
        return N
    else:
        for i in range(N-2):
            c = a+b
            a = b
            b = c
        return c
n = int(input())
while n > 0:       
    print(F(n))
    n = int(input())
    



def F(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return F(N - 1) + F(N - 2)
n = int(input())
while n > 0:
    print(F(n))
    n = int(input())
