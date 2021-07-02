class Int2Roman:
    def __init__(self, n):
        self._n = n
    def int2Roman(self):
        s = list(self._n)
        s.reverse()
        res = ""
        Units = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        Tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        Hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        Thousands = ["M", "MM", "MMM"]
        All = []
        All.append(Units)
        All.append(Tens)
        All.append(Hundreds)
        All.append(Thousands)
        for i in range(len(s)):
            res = All[i][int(s[i])-1] + res
        return res
n = input()
ir = Int2Roman(n)
print(ir.int2Roman())

"""
123
"""
