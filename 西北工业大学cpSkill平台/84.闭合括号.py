class utils:
    def __init__(self, st):
        self.st = st
    def changeSt(self, st):
        self.st = st
    def islegal(self):
        lis = []
        dic = {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            if self.st[i] == '(' or self.st[i] == '[' or self.st[i] == '{':
                lis.append(self.st[i])
            if self.st[i] == ')' or self.st[i] == ']' or self.st[i] == '}':
                if lis[len(lis)-1] == dic[self.st[i]]:
                    lis.pop()
        if len(lis) == 0:
            return True
        else:
            return False
u = utils("")
while True:
    s = input()
    if  s == "":
        break
    u.changeSt(s)
    print(u.islegal())

"""
(){}[]
()[{)}
()


"""
