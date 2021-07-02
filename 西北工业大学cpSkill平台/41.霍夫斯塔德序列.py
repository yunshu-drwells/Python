def F(n):
 if n == 0:
     return 1
 else:
     return n - M(F(n - 1))
def M(n):
 if n == 0:
     return 0
 else:
     return n - F(M(n - 1))
num = int(input())
if num >= 0:
 f = F(num)
 m = M(num)
 print(f, m, sep=" ")


 

n = int(input())
def Hofstadter_sequence(n):
    F = [i for i in range(n+1)]
    M = [i for i in range(n+1)]
    F[0] = 1
    M[0] = 0
    for i in range(1, n+1):
        M[i] = i - F[M[i-1]]
        F[i] = i - M[F[i-1]]
    return [F[n], M[n]]
u = Hofstadter_sequence(n)
if n >= 0:
    print(u[0], u[1], sep = " ")


