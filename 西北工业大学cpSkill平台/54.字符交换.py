st = str(input())
indexOfDecimalpoint = st.index(".", 0, len(st))
indexOfComma = st.index(",", 0, len(st))
st = list(st)
if(-1 != indexOfDecimalpoint):
    st[indexOfDecimalpoint] = ','
if(-1 != indexOfComma):
    st[indexOfComma] = '.'
print("".join(st))
