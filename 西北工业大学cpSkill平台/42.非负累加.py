n, v = map(int, input().split())
count = 0
for i in range(0, v + 1):
 for ii in range(0, v + 1):
     for iii in range(0, v + 1):
         for iiii in range(0, v + 1):
             for iiiii in range(0, v + 1):
                 if (i + ii + iii + iiii + iiiii) == v:
                     count += 1
print(count)
