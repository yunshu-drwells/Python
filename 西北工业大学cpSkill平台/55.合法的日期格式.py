import time
while True:
 x = input()
 if x == "":
     break
 else:
     try:
         if "-" in x:
             time.strptime(x,"%Y-%m-%d")
             print(True)
         elif "." in x:
             time.strptime(x,"%Y.%m.%d")
             print(True)
         elif "/" in x:
             time.strptime(x,"%Y/%m/%d")
             print(True)
         else:
             print(True)
     except:
         print(False)






def legal(st, s):
    L = st.split(s)
        if(L[1] <= 0 or L[1] > 12 or L[2] <= 0 or L[2] > 31):
            return False
def IsLegal(st):  
    if 2 == st.count("-", 0, len(st)):
        legal(st, "-")
        return True
    elif 2 == st.count("/", 0, len(st)):
        legal(st, "/")
        return True
    elif 2 == st.count(".", 0, len(st)):
        legal(st, ".")
        return True
    elif 2 == st.count(":", 0, len(st)):
        legal(st, ":")
        return True
    else:
        return False
while True:
    st = str(input())
    if st == "":
        break
    print(IsLegal(st))


