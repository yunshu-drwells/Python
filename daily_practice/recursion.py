# 递归
# 定义:函数内部调用函数本身


# 1.使用递归求fibonacci(1, 1, 2, 3, 5, 8, 13, 21 ,34...)
def fiboRecur(k):
    assert k>0, "k必须大于0"
    if k in [1, 2]:
        return 1
    return fiboRecur(k-1)+fiboRecur(k-2)
print("fiboRecur(7): ", fiboRecur(7))
print("fiboRecur(9): ", fiboRecur(9))


# 2.使用迭代求fibonacci
def fiboIter(k):
    assert k>0, "k必须大于0"
    if k in [1, 2]:
        return 1
    itera1 = 1
    itera2 = 1
    for _ in range(1, k-2+1):  # for循环中开始写了i, unused variable可用_代替
        tmp = itera2
        itera2 += itera1  # itera2 = itera2 + itera1
        itera1 = tmp
    return itera2
print("fiboIter(3): ", fiboIter(3))
print("fiboIter(7): ", fiboIter(7))
print("fiboIter(9): ", fiboIter(9))