list = list(input().split(" "))
n = int(input())
pr = []
flag = False
for j in range(len(list)):
    pr.append(list[(j+n)%len(list)])
print(" ".join(pr))

"""
1 2 3 4 5 6 7
2
"""
