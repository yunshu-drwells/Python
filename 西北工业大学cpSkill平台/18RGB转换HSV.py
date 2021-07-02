R = int(input())/255
G = int(input())/255
B = int(input())/255
def max(a, b, c):
    m = a if a > b else b
    m = m if m > c else c
    return m
def min(a, b, c):
    m = a if a < b else b
    m = m if m < c else c
    return m
V = maximum = max(R, G, B)
minimum = min(R, G, B)
S = (maximum - minimum)/maximum
if maximum == R:
    H = (G-B)/(V-minimum)
if maximum == G:
    H = 2+(B-R)/(maximum-minimum)
if maximum == B:
    H = 4+(R-G)/(maximum-minimum)
H *= 60
if H<0:
    H += 360
print("{:.4f}".format(H), "{:.4%}".format(S), "{:.4%}".format(V), sep = ",")
