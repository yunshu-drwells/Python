n = int(input())
def var(n):
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i+j+k+l == n:
                        print(i, j, k&l, sep = "")
                        return
var(n)
