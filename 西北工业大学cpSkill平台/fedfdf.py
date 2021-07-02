#超长发挥
formula = input()
#转换为列表找到两个符号的索引并记录
formulaList = list(formula)
for i in range(len(formulaList)):
    if formulaList[i] == '+' or formulaList[i] == '-' or formulaList[i] == '*' or formulaList[i] == '/':
        formulaList[i] = '#'
#得出xyz     
L = "".join(formulaList).split('#')
##x, y, z = map(L)
x = int(L[0])
y = int(L[1])
z = int(L[2])

#两个符号的索引
firt = formulaList.index('#')
formulaList[firt] = '&'
second = formulaList.index('#')
formulaList[firt] = '#'
formulaList = "".join(formulaList).split("#")
#运算函数
def calculate(a, b, sign):
    if sign == '*':
        return a*b
    if sign == '/':
        return a/b
    if sign == '+':
        return a+b
    if sign == '-':
        return a-b  
if formula[firt] == '*'or formula[firt] == '/':
    print(formula, "=", calculate(calculate(x, y, formula[firt]), z, formula[second]), sep="")
else:
    print(formula, "=", calculate(calculate(y, z, formula[second]), x, formula[firt]), sep="")
"""
1+2*3
"""
