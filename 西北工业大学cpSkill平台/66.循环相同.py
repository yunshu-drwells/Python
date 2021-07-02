list1 = list(input().split(" "))
list2 = list(input().split(" "))
def vv(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        pr = []
        flag = False
        for j in range(len(list1)):
            if(list1[j] == list2[(j+i)%len(list2)]):
                flag = True
            else:
                flag = False
                break
        if flag:
            return flag
    return False
print(vv(list1, list2)) 












#启示
list1 = list(input().split(" "))
list2 = list(input().split(" "))
def vv(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        pr = []
        flag = False
        for j in range(len(list1)):
            if(list1[j] == list2[(j+i)%len(list2)]):
                pr.append(list2[(j+i)%len(list2)])
                flag = True
            else:
                flag = False
                break
        print(pr)
        if flag:
            return flag
    return False
print(vv(list1, list2))        









def f(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        flag = False
        for j in range(len(list1)):
            if(list1[j] == list2[(j+i)%len(list2)]):
                flag = True
            else:
                flag = False
        if flag:
            return flag
    return False

print(vv(list1, list2))
##print(f(list1, list2))
"""
A C G T A A
A A A C G T
"""
