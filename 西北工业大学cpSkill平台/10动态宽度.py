m = int(input())
n = int(input())
def toBin(num):
    s = ""
    for i in range(0, n):
        s += str(num&1)
        num >>= 1
        l = list(s)
        l.reverse()
    return "".join(l)
print(toBin(m))

