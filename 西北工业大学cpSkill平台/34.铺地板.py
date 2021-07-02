def floor(n):
    if n%2 == 1:
        return 0
    f = [0 for i in range(n+1)]
    f[0] = 1
    f[2] = 3
    for i in range(4, n+1, 2):
        f[i] = f[i-2]*4 - f[i-4]
    return f[n]%100003

n = int(input())
while n != 0:
    print(floor(n))
    n = int(input())





MAX = 1001
s = [i for i in range(MAX)]
n = int(input())
s[0]=1
s[2]=3
for i in range(4, MAX, 2):
    s[i]=4*s[i-2]-s[i-4]
while n>0:
    if n&1:
        print(0)
    else:
        print(s[n]%100003)
    n = int(input())





maxn = 40

dp[maxn][5]

def init():
    dp[0][0] = dp[0][2] = 1
    dp[0][1] = 0
    dp[1][0] = dp[1][2] = 0
    dp[1][1] = 1
    for i in range(2, 31):
        dp[i][0] = dp[i-2][0] + dp[i-1][1] + dp[i-2][2]
        dp[i][1] = dp[i-1][2]
        dp[i][2] = dp[i-1][1] + dp[i][0]
n = 1
init()
while  n!=0:
    n = int(input())
    if n == -1:
        break;
    print(dp[n][0])

