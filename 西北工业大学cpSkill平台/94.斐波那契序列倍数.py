n, k = map(int, input().split())
f = [0, 1]
i = 2
while n:
    f_i = f[i-1] + f[i-2]  # 添加入斐波那契数列
    f.append(f_i)
    if f[i] % k == 0:
        # 每发现一个k的倍数进行n的自减
        n -= 1
    i += 1
print(len(f)-1)


















n, k = map(int, input().split())
def fib(n):
    if 0 == n:
        return 0
    if 1 == n or 2 == n:
        return 1
    a = 0
    b = 1
    c = 1
    for i in range(n-2): 
        a = b
        b = c
        c = a+b
    return c
x = 0
while k > fib(x):
    if k == fib(x):
        break
    else:
        x+=1
##print(x)
print(x*n)
##print(x*k)
    
"""
3 2
"""
