# 1.map函数# map(func, iterable) 
# 将可迭代对象依次传递给func函数处理
# 最后返回可迭代对象
def power(x):
    return x*x
res = map(power, [1, 2, 3, 4, 5])  # 返回值是生成器
print(type(res))  #map
print(list(res))

# 2.lambda表达式
print(list(map(lambda x: x*x, [1, 2, 3, 4, 5])))

#3.reduce函数
from functools import reduce  # 从模块中引入
li = [1, 2, 3, 4]
res1 = reduce(lambda x, y: x*y, li)
print(type(res1))  #int
print(res1)
# func函数必须接受两个参数,reduce会把func的运行结果作为一个参数,
# 然后从interable中依次取出一个作为另一个参数



# 4.将列表变为整数
# [1, 3, 5, 7, 9]  --> 13579
def func(x, y):
    return x*10+y
res2 = reduce(func, [1, 3, 5, 7, 9])
print(type(res2))
print(res2)
# 转换为lambda表达式
print(reduce(lambda x, y: x*10+y, [1, 3, 5, 7, 9]))


# 5.将字符串变为数字,模拟实现 int(), 用字典实现map返回可迭代对象
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]
print(reduce(func, map(char2num, '13579')))
print(int('13579'))
# 整理str2int
digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def str2int(s):
    def fn(x, y):
        return x*10+y
    def char2int(s):
        return digits[s]
    return reduce(fn, map(char2int, s))
print(str2int('1532104'))
print(int('1532104'))


# 6.filter函数
# filter(func, iterable) 根据func来过滤iterable
li1 = [1, 2, 4, 5, 7, 8, 9]
# 过滤除奇数
res3 = filter(lambda x: x%2 == 1, li)
print(type(res3))  #filter
print(list(res3))



# 7.列表推导式
li2 = []
for i in range(10):
    li2.append(i)
print(li2)

print([i for i in range(10)])  # 列表推导式快速生成列表



# 8.sorted函数
# sorted(iterable, key, reverse)
# iterable要排序的对象, key排序规则, reverse是否逆序

from random import randint  # 引入随机数模块
li3 = [randint(-10, 10) for _ in range(5)]
# randint(-10, 10)生成值在[-10, 10]中的随机数
print(li3)
# 排序
res4 = sorted(li)  #reverse默认False, 升序
print(res4)
# key-->按照绝对值排序
res4 = sorted(li, key=abs)  # abs系统默认函数
print(res4)
# 降序排序
res4 = sorted(li, key=abs, reverse=True)
print(res4)







