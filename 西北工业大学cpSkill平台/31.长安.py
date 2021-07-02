l1 = []


def fun(m, n):
    t1 = 1
    t2 = 1
    t3 = n
    t4 = m
    while t3 > 0:  # t1
        t1 *= t4
        t4 -= 1
        t3 -= 1
    t3 = n
    while t3 > 0:  # t2
        t2 *= t3
        t3 -= 1
    return t1 // t2


while True:
    x = input()
    bi, bj, pi, pj = map(int, x.split(","))
    if bi < 0 or bj < 0 or pi < 0 or pj < 0:
        break
    else:
        a = fun((bi + bj), bj)
        b = fun((pi + pj), pj)
        c = fun((abs(bi - pi) + abs(bj - pj)), abs(bj - pj))
        if b == 1 or c == 1:
            d = a
        else:
            d = a - b * c
        l1.append(d)
for i in range(0, len(l1)):
    print(l1[i])
