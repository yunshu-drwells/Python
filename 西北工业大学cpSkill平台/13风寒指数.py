import math
v = float(input())
t = float(input())
chill = 13.12+0.6215*t-11.37*math.pow(v, 0.16)+0.3965*t*math.pow(v, 0.16)
print(round(chill))
