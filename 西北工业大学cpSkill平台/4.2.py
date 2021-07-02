a = int(input())
b = int(input())
def toBin(num):
    s = ""
    while num > 0:
        s += str(num&1)
        num >>= 1
        l = list(s)
        l.reverse()
    return "".join(l)
print("0b"+toBin(a))
print("0b"+toBin(b))
