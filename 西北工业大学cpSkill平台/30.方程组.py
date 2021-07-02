a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a/d == b/e and a/d != c/f:
    print("error")
else:
    x=(c*e-f*b)/(a*e-d*b)
    y=(c*d-a*f)/(b*d-e*a)
    print("{:.3f}".format(x), "{:.3f}".format(y), sep = " ")
