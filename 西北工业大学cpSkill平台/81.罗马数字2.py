#远
def RomanInt2Int(str):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = 0
    for i in range(len(str) - 1):
        if d[str[i]] < d[str[i + 1]]:
            count -= d[str[i]]
        else:
            count += d[str[i]]
    count += d[str[len(str) - 1]]
    return count if 1 < count < 3999 else False
str = input()
print(RomanInt2Int(str))

"""
CXXIII
"""
#{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}











#孙豪
class RomanInt:
    def __init__(self, s):
        self.s = s
    def fun(self):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(self.s) - 1):
            if d[self.s[i]] < d[self.s[i + 1]]:
                result -= d[self.s[i]]
            else:
                result += d[self.s[i]]
        result += d[self.s[len(self.s) - 1]]
        return result if 1 < result < 3999 else False
x = input()
a = RomanInt(x)
print(a.fun())

