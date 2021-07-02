def Hofstadter_sequence(n):
    F = [i for i in range(n+1)]
    M = [i for i in range(n+1)]
    F[0] = 1
    M[0] = 0
    for i in range(1, n+1):
        M[i] = i - F[M[i-1]]
        F[i] = i - M[F[i-1]]
    return [F[n], M[n]]


def F(n):
  if n == 0:
     return 1
  else:
      ret = n - M(F(n - 1))
      return ret


def M(n):
    if n == 0:
        return 0
    else:
        ret = n - F(M(n - 1))
        return ret




for n in range(0, 10000):
    u = Hofstadter_sequence(n)
    if u[0] != F(n) or u[1] != M(n):
        print(F(n), M(n), u[0], u[1], sep = " ")
print("same")
