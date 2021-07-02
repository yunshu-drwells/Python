def f(st):
    indexOfNot = st.find("not")
    indexOfPoor = st.find("poor")
    if indexOfNot >= 0 and indexOfPoor > indexOfNot:
        return st[0:indexOfNot]+"good"+st[indexOfPoor+4:len(st)]
    else:
        return st
while True:
    st = input()
    if st == "":
        break
    print(f(st))
"""
The table is not that poor!
The table is poor!
The table is good!
"""
