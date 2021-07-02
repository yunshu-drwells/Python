while True:
    st = input()
    if st == "":
        break
    if len(st) < 2:
        print(st)
    else:
        print(st[0:2]+st[len(st)-2:len(st)])
