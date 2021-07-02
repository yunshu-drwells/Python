import math
n = int(input())
m = int(input())
sum = 0
for i in range(m):
    sum += n*int(math.pow(10, i))*(m-i)
print(sum)

# 解法为按位计算，第一次循环统计各位，第二次十位以此类推...每一位的个数随循环减少
# 555
#  55
#   5

# pow(10, i)效率还可以提升，利用迭代
sum = 0
tmp = 1
for i in range(m):
    sum += n*tmp*(m-i)
    tmp *= 10
print(sum)
