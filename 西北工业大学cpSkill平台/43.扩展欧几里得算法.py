def gcd(x, y):
 i = x
 while i > 1:
     if x % i == 0 and y % i == 0:
         return i
     i -= 1
 else:
     return 1
def fun(x, y):
 t = gcd(x, y)
 i = 0
 j = 0
 while True:
     j = (t - x * i) // y
     if t == x * i + y * j:
         return i, j
     i += 1
x = input()
a, b = map(int, x.split())
ret1, ret2 = fun(a, b)
print(ret1, ret2, sep=" ")






a, b = map(int, input().split())
# 得出最大公约数
def MaxDivisor(d):
    a = d[0]
    b = d[1]
    while a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    return b
acb = MaxDivisor([a, b])
#求值
def fun(a, b, acb):
    x = 1
    y = 0
    while True:
        y = (acb-x*a)//b
        if acb == a*x+b*y:
            return x, y
        x += 1
x, y = fun(a, b, acb)
print(x, y, sep = " ")

