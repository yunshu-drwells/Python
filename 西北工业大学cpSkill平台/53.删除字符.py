while True:
    st = str(input())
    if st == "":
        break
    L = list(st)
    end = len(st)>>1
    i = 1
    for index in range(0, end):
            del L[i]
            i+=1
    print(''.join(L))
