##13901011667
##18002911667
##119
import re
def legitimated(phoneNumber):
    if len(phoneNumber) < 11 or len(phoneNumber) >11:
        return False
    netBios = phoneNumber[0:2]
    for c in phoneNumber:
        if c < '0'or c > '9':
            return False
    if re.match(r'13[0,1,2]\d{8}',phoneNumber) or \
            re.match(r"15[5,6]\d{8}",phoneNumber) or \
            re.match(r"18[5,6]",phoneNumber) or \
            re.match(r"145\d{8}",phoneNumber) or \
            re.match(r"176\d{8}",phoneNumber):
        print("该号码属于：中国联通")
        return True
    if re.match(r"13[4,5,6,7,8,9]\d{8}",phoneNumber) or \
            re.match(r"147\d{8}|178\d{8}",phoneNumber) or \
            re.match(r"15[0,1,2,7,8,9]\d{8}",phoneNumber) or \
            re.match(r"18[2,3,4,7,8]\d{8}",phoneNumber):
        print("该号码属于：中国移动")
        return True
    if re.match(r"133\d{8}",phoneNumber) or \
            re.match(r"149\d{8}",phoneNumber) or \
            re.match(r"153\d{8}",phoneNumber) or \
            re.match(r"177\d{8}",phoneNumber) or \
            re.match(r"18[0,1，9]\d{8}",phoneNumber):
        print("该号码属于：中国电信")
        return True
    return Flase
phoneNumber = str(input())
print(legitimated(phoneNumber))








import re
def legitimated(phoneNumber):
    if len(phoneNumber) < 11 or len(phoneNumber) >11:
        return False
    netBios = phoneNumber[0:2]
    for c in phoneNumber:
        if c < '0'or c > '9':
            return False
    if re.match(r'13[0,1,2]\d{8}',phoneNumber) or \
            re.match(r"15[5,6]\d{8}",phoneNumber) or \
            re.match(r"18[5,6]",phoneNumber) or \
            re.match(r"145\d{8}",phoneNumber) or \
            re.match(r"176\d{8}",phoneNumber) or \
            re.match(r"13[4,5,6,7,8,9]\d{8}",phoneNumber) or \
            re.match(r"147\d{8}|178\d{8}",phoneNumber) or \
            re.match(r"15[0,1,2,7,8,9]\d{8}",phoneNumber) or \
            re.match(r"18[2,3,4,7,8]\d{8}",phoneNumber) or \
            re.match(r"133\d{8}",phoneNumber) or \
            re.match(r"149\d{8}",phoneNumber) or \
            re.match(r"153\d{8}",phoneNumber) or \
            re.match(r"177\d{8}",phoneNumber) or \
            re.match(r"18[0,1，9]\d{8}",phoneNumber):
        return True
    return Flase
phoneNumber = str(input())
print(legitimated(phoneNumber))







while True:
    num = input()
    if num == "":
        break
    l = ['13', '14', '15', '18', '17', '19']
    flag = False
    if num[:2] in l and len(num) == 11:
        flag = True
    else:
        flag = False
    print(flag)
 



def legitimated(phoneNumber):
    right = ["13", "14", "15", "17", "18", "19"]
    #判断位数是否合理
    if len(phoneNumber) < 11 or len(phoneNumber) >11:
        return False
    netBios = phoneNumber[0:2]
    #判断是否有除数字以外的字符
    for c in phoneNumber:
        if c < '0'or c > '9':
            return False
    #判断号码前两位是否合理
    for st in right:
        if st == netBios:
            return True
    return Flase
while True:
    phoneNumber = str(input())
    if phoneNumber != "":
        print(legitimated(phoneNumber))
    else:
        break


