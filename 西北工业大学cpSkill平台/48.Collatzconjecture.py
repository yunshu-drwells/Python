n = int(input())
def Collatz(n):
    Col = [n]
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n=3*n+1
        Col.append(n)
    return Col
for i in Collatz(n):
    if 1 != i:
        print(i, end = ",")
    else:
        print(i)
