#字符串切片
n = int(input())
st = str('{:b}'.format(n))
result = st[::-1]
print(result)


#列表的reverse
n = int(input())
st = str('{:b}'.format(n))#二进制转字符串
l = list(st)#字符串转换成列表
l.reverse()#翻转列表
print(''.join(l))#连接字符串并打印


#reduce
from functools import reduce
n = int(input())
st = str('{:b}'.format(n))
l = list(st)
result = reduce(lambda x,y:y+x,l)
print(result)


#使用递归函数
def func(s):
    if len(s) <1:
        return s
    return func(s[1:])+s[0]

n = int(input())
st = str('{:b}'.format(n))
result = func(st)
print(result)


#for循环
def func(s):
    result = ""
    max_index = len(s)-1
    for index,value in enumerate(s):
        result += s[max_index-index]
    return result
n = int(input())
st = str('{:b}'.format(n))
result = func(st)
print(result)
