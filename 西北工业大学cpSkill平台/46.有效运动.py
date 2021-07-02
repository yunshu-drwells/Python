x1, y1, x2, y2 = map(int, input().split())
def f(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    if x1 > x2 or y1 > y2:
        return False
    else:
        return f(x1+y1, y1, x2, y2) or f(x1, y1+x1, x2, y2)
if f(x1, y1, x2, y2):
    print("true")
else:
    print("false")
# 2 10 26 12
##f(14 10 26 12) or f(2 12 26 12)
##...  f(14 12 26 12) or f(2 14 26 12)
##... ... ... f(26 12 26 12) or f(14 26 26 12)
