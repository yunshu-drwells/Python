n = int(input())
# n!/(n-a)!
def fact(n, a):
        pro = 1
        tmp = n
        for i in range(a): #n*(n-1)*...*n-a+1
            pro *= tmp
            tmp -= 1
        return pro
#n!
def factorial(n):
        pro = 1
        for i in range(n, 0, -1):
            pro *= i
        return pro
print(fact(2*n, n)//factorial(n+1))
