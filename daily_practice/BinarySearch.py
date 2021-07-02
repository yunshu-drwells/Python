# 二分查找(递归版recursion)
from random import randint, choice
data = [randint(1, 100) for _ in range(10)]  # 列表推导式生成10个随机数
# 随机选择一个
target = choice(data)  # 要查找的数
data = sorted(data)  # 二分查找的前提是有序

def binSearchRecursion(left, right, dataList, target):
    mid = int((right - left)/2)+left # mid = int((left+right)/2)
    if target == dataList[mid]:
        return mid
    elif target > dataList[mid]:
        return binSearchRecursion(mid+1, right, dataList, target)
    else:
        return binSearchRecursion(left, mid - 1, dataList, target)

resIndex = binSearchRecursion(0, len(data)-1, data, target)
print("所查找的有序列表: ", data)
print("所查找的", target, "下标是:", resIndex)




# 二分查找(非递归)
def binSearch(dataList, target):
    left = 0
    right = len(dataList)-1
    while left <= right:
        mid = int((right - left)/2)+left # mid = int((left+right)/2)
        if target == dataList[mid]:
            return mid
        elif target > dataList[mid]:
            right = mid + 1
        else:
            left = mid - 1

resIndex = binSearch(data, target)
print("所查找的有序列表: ", data)
print("所查找的", target, "下标是:", resIndex)

