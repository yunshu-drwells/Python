n = int(input())
product = 1
for i in range(1, n+1):
    product *= i
num = 0
for i in range(len(str(product))):
    if('0' == str(product)[len(str(product))-i-1]):
        num+=1
    else:
        break
print(num)
