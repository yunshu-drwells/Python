# a!/(a-n)!
def factorial(n, a):
        pro = 1
        tmp = n
        for i in range(a):
            pro *= tmp
            tmp -= 1
        return pro
# b!/a!*(b-a)!
def c(a, b):
    return factorial(a+b, a)/factorial(a, a)
def cout(bx, by, px, py):
    if px <= bx and py <= by:
        return c(bx, by) - c(px, py)*c(bx-px, by-py)
    else:
        return c(bx, by)
bx = by = px = py = 1
L = []
while True:
    bx,by,px,py = map(int,input().split(","))
    if bx>=0 and by>=0 and px>=0 and py>=0:
        L.append(int(cout(bx, by, px, py)))
    else:
        break
for i in range(0, len(L)):
    print(L[i])
