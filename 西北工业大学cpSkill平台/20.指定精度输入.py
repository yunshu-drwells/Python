f = float(input())
n = int(input())
s = str(f)[0:len(str(int(f)))+n+2]
if(int(s[len(s)-1])>4):
    s2 = str(int(s[len(s)-2])+1) 
else:
    s2 = str(int(s[len(s)-2]))
s = s[0:len(str(int(f)))+n]+s2
print(s)
