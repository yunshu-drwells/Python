n = int(input())
count = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
                d = n-a-b-c
                if 0 <= d <= 9:
                    count += 1
print(count)
