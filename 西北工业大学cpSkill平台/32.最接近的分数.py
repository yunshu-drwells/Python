n, a, b = map(int,input().split(" "))
p = 1
q = n
def most_common_divisor(d):
    a = d['numerator']
    b = d['denominator']
    if a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    if b == d['denominator']:
        return False
    else:
        return True
value = a/b
gap_min = 1001
result_deno = 1
result_nume = 0
for denominator  in range(1, n+1):
    numerator = int(denominator * value)
    gap = abs(numerator/denominator - value)
    max = {'numerator':numerator, 'denominator':denominator}
    if gap < gap_min and gap != 0 and ~most_common_divisor(max):
        gap_min = gap
        result_deno = max['denominator']
        result_nume = max['numerator']
print(result_nume, '/', result_deno, sep='')










n, a, b = map(int,input().split(" "))
p = 1
q = n
def simple(d):
    a = d['molecule']
    b = d['denominator']
    while a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    d['molecule'] /= b
    d['denominator'] /= b
for x in range(1, 101):
    for y in range(100, 0, -1):
        if(b * x < a * y and x * q > p * y):
           p = x
           q = y
max = {'molecule':p, 'denominator':q}
simple(max)
print(str(int(max['molecule']))+"/"+str(int(max['denominator'])))








#暴力枚举分子[1, n] 分母[n, 1]
n, a, b = map(int,input().split(" "))
p = 1
q = n
for x in range(1, n+1):
    for y in range(n, 0, -1):
        if(b * x < a * y and x * q > p * y):
           p = x
           q = y
print(str(p)+"/"+str(q))










n = int(input())
a = int(input())
b = int(input())
def simple(d):
    a = d['molecule']
    b = d['denominator']
    while a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    d['molecule'] /= b
    d['denominator'] /= b
dict = {'molecule':a, 'denominator':b}
i = 0
c = dict['denominator']
while(True):
    c = dict['denominator']
    c = dict['denominator']*i
    if dict['denominator']*(i+1)>n:
        break
    i+=1
print("++",i)
dict['molecule'] *= i
dict['denominator'] *= i
for x in range(dict['molecule'], n+1):
    for y in range(n, 0, -1):
        if(b*x<a*y and x*max['denominator']>max['molecule']*y):
           max['molecule'] = x
           max['denominator'] = y
simple(max)
print(int(max['molecule']),"/",int(max['denominator']))
