



class ReverseString:
    def __init__(self, str):
        self._str = str
    def reverseStr(self):
        res = ""
        L = self._str.split(" ")
        L.reverse()
        return " ".join(L)
st = input()
rs = ReverseString(st)
print(rs.reverseStr())

"""
hello npu
"""












#超常发挥
class ReverseString:
    def __init__(self, str):
        self._str = str
    def reverseWord(self, st):
        L = []
        for i in st:
            L.append(i)
        L.reverse()
        return "".join(L)
    def reverseStr(self):
        res = ""
        L = self._str.split(" ")
        L.reverse()
        for i in range(len(L)):
            L[i] = self.reverseWord(L[i])
        return " ".join(L)
st = input()
rs = ReverseString(st)
print(rs.reverseStr())

"""
hello npu

upn olleh
"""
