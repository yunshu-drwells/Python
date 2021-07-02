integer = int(input())
def isSymmetry(a, b):
    if (a=='9'and b=='6') or (a=='6'and b=='9') or a == b:
        return True
    else:
        return False
flag = True
for i in range(len(str(integer))>>1):
    if False == isSymmetry(str(integer)[i], str(integer)[len(str(integer))-i-1]):
        flag = False
if flag:
    print("Yes")
else:
    print("No")
