Q = int(input())
for divisor in range(10, 100, 1):
    Dividend = divisor*Q + 1
    if(Dividend < 10000):
        print(Dividend, divisor, sep = " ")

"""
709
"""

"""
F/D = Q ...1
100 <= Q <= 1000
"""
