def f(st):
    parts = st.split(".")
    if int(parts[0]) > 255 or int(parts[0]) < 1:
        return False
    for i in range(1, len(parts)):
        if int(parts[i]) > 255 or int(parts[i]) < 0:
            return False
    return True
while True:
    st = input()
    if st == "":
        break
    print(f(st))
    
