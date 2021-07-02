#方一舟
import re
def url(string: str) -> list :
    # 含括号匹配时不作处理仅返回括号内容
    # 在括号前假设?:后返回所有元素
    result = re.findall(r'(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', string)
    return result
st = input()
print(url(st))
"""
The latest news web is https://news.nwpu.edu.cn/info/1002/70871.htm, not https://www.nwpu.edu.cn/
"""






#正则表达式求URL
import re
def Find(string):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url 
st = input()
n = st.count("https://")
rest = st[:]
https = []
while rest.count("https://")>0:
    https.append(rest[rest.rfind("https://"):len(rest)])
    rest = rest[0:rest.rfind("https://")]
for i in range(len(https)):
    https[i] = Find(https[i])[0]
print(https) 






#error
st = input()
n = st.count("https://")
rest = st[:]
https = []
while rest.count("https://")>0:
    https.append(rest[rest.rfind("https://"):len(rest)])
    rest = rest[0:rest.rfind("https://")]
for i in range(len(https)):
    if https[i].count(".htm") > 0:
        https[i] = https[i][0:https[i].rfind(".htm")+4]
    elif https[i].count(".cn/") > 0:
        https[i] = https[i][0:https[i].rfind(".cn/")+4]
https.reverse()
print(https) 

"""
The latest news web is https://news.nwpu.edu.cn/info/1002/70871.htm,nothttps://www.nwpu,edu.cn/
"""
