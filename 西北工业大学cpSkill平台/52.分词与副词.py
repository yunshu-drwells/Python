while True:
    st = str(input())
    if st == "":
        break
    if len(st) < 3:
        print(st)
    elif st[len(st)-3 : len(st)] == "ing":
        print(st+"ly")
    else:
        print(st+"ing")
