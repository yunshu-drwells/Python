n = int(input())
def fib(n):
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
print(fib(n))
