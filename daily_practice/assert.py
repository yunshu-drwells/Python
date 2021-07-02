# 断言格式
# assert 表达式 [, 参数]
def div(s):
    n = int(s)
    assert n!=0 , "除数不能为0"
    return 10/n
print(div('0'))