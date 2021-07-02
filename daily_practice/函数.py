# def 函数名 参数列表:
    # 函数体

# 一个简单的函数
def sayHello1():
    print("hello")
# 调用函数
sayHello1()

# 带参的函数
def sayHello2(name):  
    
    print('你好', name)
    print("type of name is", type(name))
sayHello2("武汉")

# 带返回值的函数
def caculateNum(num):
    result = 0
    for i in range(1, num+1):
        result += i  # result = result + i
    return result
res = caculateNum(100) # 5050
print(res)
