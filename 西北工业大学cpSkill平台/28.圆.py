import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a=2*(x2-x1)
b=2*(y2-y1)
c=2*(x3-x2)
d=2*(y3-y2)
e=x2*x2+y2*y2-x1*x1-y1*y1
f=x3*x3+y3*y3-x2*x2-y2*y2
x=(b*f-d*e)/(b*c-d*a)
y=(c*e-a*f)/(b*c-d*a)
r=math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
print("{:.3f}".format(r), "{:.3f}".format(x), "{:.3f}".format(y), sep = ",")



a=2*(x2-x1)
b=2*(y2-y1)
c=x2*x2+y2*y2-x1*x1-y1*y1
d=2*(x3-x2)
e=2*(y3-y2)
f=x3*x3+y3*y3-x2*x2-y2*y2
x=(b*f-e*c)/(b*d-e*a)
y=(d*c-a*f)/(b*d-e*a)
r=math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
print(r, x, y)




