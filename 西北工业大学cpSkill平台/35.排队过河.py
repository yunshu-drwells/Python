def Jump(s, y):
    k = 0
    if s == 0:
        k = y + 1
    else:
        k = 2 * Jump(s - 1, y)
    return k
s,y = map(int,input().split(","))
while(-1 != s and -1 != y):
    sum = Jump(s, y)
    print(sum)
    s,y = map(int,input().split(","))


    
#error
def Jump(s, y):
    k = 0
    if s == 0:
        k = y + 1
    else:
        k = 2 * Jump(s - 1, y)
    return k
s,y = map(int,input().split(","))
sum = Jump(s, y)
print(sum)





