n = int(input())
def count(n):
    sum = 0
    while(n > 0):
        sum += int(n%10)
        n /= 10
    return sum
nums = 0
while n>0:
    n -= count(n)
    nums += 1
print(nums)
