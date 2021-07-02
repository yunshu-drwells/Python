import math
x = float(input())
y = float(input())
print("{:.4f}".format(math.sqrt(pow(x, 2)+pow(y, 2))), "{:.4f}".format(math.atan2(y, x)), sep = ",")
