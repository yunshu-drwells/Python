
##舟right
import time
startTicks = time.time()

def number(n):
    for a1 in range(n, 0, -1):
        for a2 in range(n, 0, -1):
            if (a1+a2)%2 != 0:
                continue
            for a3 in range(n, 0, -1):
                if  (a2+a3)%3 == 0 and (a1+a2+a3)%5 == 0:
                    max = a1+a2+a3
                    return max

n = int(input())
print(number(n))

endTicks = time.time()
print(endTicks - startTicks)




##right timeout
import time
startTicks = time.time()

n = int(input())
max = 0
range1 = n*3 - ((n*3)%5)
range2 = 2*n - ((n*2)%3)
range3 = 2*n - ((n*2)%2)
for a1Aa2Aa3 in range(range1, 0, -5):
    for a2Aa3 in range(range2, 0, -3):
        if a1Aa2Aa3 - a2Aa3 > n:
            continue
        for a1Aa2 in range(range3, 0, -2):
            if a2Aa3 + a1Aa2 - a1Aa2Aa3 <= n  and a1Aa2Aa3 - a1Aa2 <= n:
                if(max < a1Aa2Aa3):
                    max = a1Aa2Aa3
print(max)

endTicks = time.time()
print(endTicks - startTicks)









##right timeout
import time
startTicks = time.time()

n = int(input())
max = 0
for a1Aa2Aa3 in range(n*3 - ((n*3)%5), 0, -5):
    for a2Aa3 in range(2*n - ((n*2)%3), 0, -3):
        for a1Aa2 in range(2*n - ((n*2)%2), 0, -2):
            if a2Aa3 + a1Aa2 - a1Aa2Aa3 <= n and a1Aa2Aa3 - a2Aa3 <= n and a1Aa2Aa3 - a1Aa2 <= n:
                if(max < a1Aa2Aa3):
                    max = a1Aa2Aa3
##                    print(a1Aa2Aa3 - a2Aa3, a2Aa3 + a1Aa2 - a1Aa2Aa3, a1Aa2Aa3 - a1Aa2, a1Aa2Aa3)
print(max)

endTicks = time.time()
print(endTicks - startTicks)







##right timeout
import time
startTicks = time.time()
n = int(input())
max = 0
range1 = n*3 - ((n*3)%5)
range2 = 2*n - ((n*2)%3)
range3 = 2*n - ((n*2)%2)
for a1Aa2Aa3 in range(range1, 0, -5):
    for a2Aa3 in range(range2, 0, -3):
        for a1Aa2 in range(range3, 0, -2):
            if a2Aa3 + a1Aa2 - a1Aa2Aa3 <= n and a1Aa2Aa3 - a2Aa3 <= n and a1Aa2Aa3 - a1Aa2 <= n:
                if(max < a1Aa2Aa3):
                    max = a1Aa2Aa3
##                    print(a1Aa2Aa3 - a2Aa3, a2Aa3 + a1Aa2 - a1Aa2Aa3, a1Aa2Aa3 - a1Aa2, a1Aa2Aa3)
print(max)
endTicks = time.time()
print(endTicks - startTicks)






##right timeout
import time
startTicks = time.time()
n = int(input())
max = 0
for a1Aa2Aa3 in range(5, n*3+1, 5):
    for a2Aa3 in range(3, 2*n+1, 3):
        for a1Aa2 in range(2, 2*n+1, 2):
            if a2Aa3 + a1Aa2 - a1Aa2Aa3 <= n and a2Aa3 + a1Aa2 - a1Aa2Aa3 >= 0:
                if(max < a1Aa2Aa3):
                    max = a1Aa2Aa3
##                    print(a1Aa2Aa3 - a2Aa3, a2Aa3 + a1Aa2 - a1Aa2Aa3, a1Aa2Aa3 - a1Aa2, a1Aa2Aa3)
print(max)
endTicks = time.time()
print(endTicks - startTicks)    












## error
n = int(input())
max = 0
for a1Aa2Aa3 in range(5, n*3+1, 5):
    if((2/5 * a1Aa2Aa3) <= n):
        max = a1Aa2Aa3
print(max)
# 符合要求的a1、a2、a3符合221离散分布






## error
n = int(input())
max = 0
for a1Aa2Aa3 in range(5, n*3+1, 5):
    if max < a1Aa2Aa3:
        max = a1Aa2Aa3
print(max)
    
##    for a1Aa2 in range(2, 2*n+1, 2):
##        for a2Aa3 in range(3, 2*n+1, 3):
##
##            a1 + a2 + a3 = 


##            a2 = a1Aa2 + a2Aa3 - a1Aa2Aa3
##            a3 = a1Aa2Aa3 - a1Aa2
##            a1 = a1Aa2Aa3 - a2Aa3





## error
import time
startTicks = time.time()
n = int(input())
max = 0
for a1 in range(0, n+1):
    for a2 in range(0, n+1):
        if (a1+a2)%2 == 0:
            for a3 in range(0, n+1):
                if(a2+a3)%3 == 0 and (a1+a2+a3)%5 == 0:
                    if max < a1+a2+a3:
                        max = a1+a2+a3
print(max)
endTicks = time.time()
print(endTicks - startTicks)






##right timeout
import time
startTicks = time.time()
n = int(input())
max = 0
for a1 in range(0, n+1):
    for a2 in range(0, n+1):
        for a3 in range(0, n+1):
            if (a1+a2)%2 == 0 and (a2+a3)%3 == 0 and (a1+a2+a3)%5 == 0:
                if(max < a1+a2+a3):
                    max = a1+a2+a3
print(max)
endTicks = time.time()
print(endTicks - startTicks)
