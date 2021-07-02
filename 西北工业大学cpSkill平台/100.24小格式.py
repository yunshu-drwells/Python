#others
def func(s):
    w = s[-2:]
    h = int(s[:2])
    T = None
    if w.lower() == "am":
        if h == 12:
            h = '00'
            T = h + s[2:-2]
        else:
            T = s[:-2]
    elif w.lower() == "pm":
        if h == 12:
            T = s[:-2]
        else:
            h = h + 12
            T = str(h) + s[2:-2]
    else:
        pass
    return T


if __name__ == '__main__':
    timeAPM = input().split(" ")
    T = func("".join(timeAPM))
    print(T)

"""
12:05:45 PM
"""





#self right
timeAPM = input().split(" ")
if timeAPM[1] == "AM":
    lis = timeAPM[0].split(":")
    if int(lis[0]) == 12:
        lis[0] = "00"
    print(":".join(lis))
elif timeAPM[1] == "PM":
    lis = timeAPM[0].split(":")
    if int(lis[0]) != 12:
        lis[0] = str((int(lis[0]) + 12)%24)
    print(":".join(lis))

"""
08:05:45 PM
"""









#self right
timeAPM = input().split(" ")
lis = timeAPM[0].split(":")
if int(lis[0]) == 12 and timeAPM[1] == "AM":
    lis[0] = "00"
elif int(lis[0]) != 12 and timeAPM[1] == "PM":
    lis[0] = str((int(lis[0]) + 12)%24)
print(":".join(lis))

"""
12:05:45 AM
"""


