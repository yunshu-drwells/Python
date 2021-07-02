# 找出100到999之间所有的水仙花数1, int数字通过除和模运算获取每一位
print("找出100到999之间所有的水仙花数1:")
targetList = []
for x in range(100, 1000):  # [100, 1000)左闭右开
    result = pow(int(x%10), 3)+pow(int(x/10%10), 3)+pow(int(x/100), 3)
    if result == x:
        targetList.append(x)
print(targetList)


# 找出100到999之间所有的水仙花数2, 将int转为str,通过索引找到每一位再将每一位转为int计算
print("找出100到999之间所有的水仙花数2:")
targetList = []
for x in range(100, 1000):  # [100, 1000)左闭右开
    result = pow(int(str(x)[0]), 3)+pow(int(str(x)[1]), 3)+pow(int(str(x)[2]), 3)
    if result == x:
        targetList.append(x)
print(targetList)
print()


# 判断任意值的一个数是不是水仙花数
num = input('请任意输入一个数: ')
length = len(num) # num位数
result = 0
for x in range(length):  #[0, length)
    result += pow(int(num[x]), 3)
print(result)
if result == int(num):
    print(num, "是水仙花数")