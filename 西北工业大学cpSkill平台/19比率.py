f = float(input())
# 分数通分
def simple(d):
    a = d['molecule']
    b = d['denominator']
    while a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    d['molecule'] /= b
    d['denominator'] /= b
# 判断小数位有几位
len = len(str(f))-len(str(int(f)))-1
dict = {'molecule':f*pow(10, len), 'denominator':pow(10, len)}
simple(dict)
print(str(int(dict['molecule']))+"/" + str(int(dict['denominator'])))



# 判断是否是整数
def isDigit(num):
    numstr = str(num).strip().lstrip('+').lstrip('-')
    if str(num).isdigit():
        return True
    else:
        return False
