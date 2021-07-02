integer = int(input())
def isSymmetry(a, b):
    if a == b:
        return True
    else:
        return False
flag = True
for i in range(len(str(integer))>>1):
    if False == isSymmetry(int(str(integer)[i]), int(str(integer)[len(str(integer))-i-1])):
        flag = False
if flag:
    print("Yes")
else:
    print("Not")


n = int(input())
s = str(n)
res = ""
for i in range(len(str(n))):
    res += str(s[i])
if int(res) == n:
    print("Yes")
else:
    print("Not")   

