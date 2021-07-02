import math
a = int(input())
b = int(input())
max = a if a>b else b
min = a if a<b else b
def isTriangle(a, b, c):
    if a+b > c and a+c > b and b+c > a and abs(a-b) < c and abs(a-c) < b and abs(c-b) < a:
        return True
    else:
        return False
condition1 = int(math.sqrt(math.pow(max, 2) - math.pow(min,2)))
condition2 = int(math.sqrt(math.pow(max, 2) + math.pow(min,2)))
if(isTriangle(min, max, condition2) and math.pow(min, 2)+math.pow(max, 2) == math.pow(condition2, 2) and condition2 > max):
        print("c")
elif(isTriangle(min, max, condition1) and  math.pow(min, 2)+math.pow(condition1, 2) == math.pow(max, 2) ):
    if condition1<min:
        print("a")
    if condition1<max and condition1>min:
        print("b")
else:
    print("non")



def isTriangle(a, b, c):
    if a+b < c:
        return False
    if a+c < b:
        return False
    if b+c < a:
        return False
    if abs(a-b) > c:
        return False
    if abs(a-c) > b:
        return False
    if abs(c-b) > a:
        return False
    return True

