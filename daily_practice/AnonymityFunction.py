# 匿名函数
# 函数名 = lambda parameter_list(参数列表): expression(表达式)
cal = lambda x, y: x*y
print(cal(4, 5))

def calc(x, y) :
    if x >= y :
        return  x*y
    else:
        return x/y
print(calc(5, 2))
# 改写成匿名形式
# 会用到:三元表达式
# if返回值 if True else False返回值
calc2 = lambda x, y: x*y if x>=y else x/y
print(calc2(5,2))

