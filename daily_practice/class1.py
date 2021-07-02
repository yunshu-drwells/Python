# 1.打印
print ('hello')  
print ("hello")  
# 限制字符串的单双引号功能一样
# 原因是为了方便在字符串中加单双引号时不用转义字符,如下:
my_str = ' I\'m a student'
my_str1 = " I'm a student" # 单双引号的混用是为了减少转义字符的使用
my_str2 = "jason said: \"you are a excellent programmer\" "
my_str3 = 'jason said: "you are a excellent programmer" '  

print(my_str)
print(my_str1)
print(my_str2)
print(my_str3)


# python2和python3的显著区别是python3中print需要加()


# 2.注释 #开头


# 3.变量及判断类型
# 声明不用加类型
怒骂 = 1000  # 变量名也可以是汉字,unicode编码的原因
num = 100
print(num)
print(怒骂)
print(type(num))


# 4.交换两个变量的值
a = 998
b = 666
print(a, b)
a,b = b,a  #交换
print(a, b)


# 5.VSCode中校验代码规范的插件



# 6.常用数据类型: 字符串,数字, 列表和元组, 字典, 集合
# 字符串
name = 'zhangsan'
name1 = "lisi"
print(name, name1)
# bool
male = True  # true的T大写
print(male)
print(type(male))
# 列表
# 列表list:和C语言中的数组比较像,可以存放不同类型的数据
heroList = ['鲁班七号', '狄仁杰', '后羿', 100, [999,99.9]]
print(heroList)  
print(type(heroList))
# 在java中数组是引用类型,需要打印就得使用toString方法改写,或者用下标索引的方式迭代
# (1)查看列表元素总个数
print(len(heroList)) 
# (2)数单个元素出现次数
print("100出现的次数:", heroList.count(100))
print("[999,99.9]出现的次数:", heroList.count([999,99.9]))
# python中长度是内置函数len访问列表元素个数, 类似的还有数元素出现次数的cout函数
# java中length是数组实例对象的属性, 通过数组对象+.length访问
# (3)访问元素:通过索引访问,首元素下标:从0开始
print(heroList[1])
# (4)修改元素
heroList[1] = '伽罗'
# (5)增加: append
heroList.append('陈咬金')
# (5)删除: del
del heroList[1]  # 删除第二个元素
print(heroList)



# 7.列表和字符串的切片
# 变量[起始:终止:步长] 左闭右开[ : : )
name2 = 'Voidcctvoureye'
list1 = ['I', 'I', 'like', 'love', 'Java', 'python']
print(name2[:4])  #起始默认0步长默认1
print(name2[4])  #省略冒号就成了索引
print(name2[4:8]) #步长默认1
print(name2[0::2])  #省略终止, 默认访问到尾


# 8.元组tuple:不能修改(安全,效率高)
a = (1, 3, 'kk')
b = (1,)  # 只有一个元素的元组要在尾部加,
print("元组a:", a)
print("元组b:",b)
print(type(a))
print("a[0] : ", a[0])  # 通过下标访问


# 9.字典dict,键值对存储
info  = {'name':'liyan', 'addr':'辽宁沈阳', 'phone':15140266200}
print(info)
print("type(info):", type(info))
# 访问元素:
print(info['addr'])  #通过键访问
# 修改
info['name'] = '李岩'
# 删除 del
del info['name']
# 添加
info['gender'] = 'female'
print(info)
# 获取所有的键(list)
print("keys : ", info.keys())
# 获取所有的值(list)
print("values : ", info.values())
# 获取所有键值对(tuple为元素的list)
print("items : ", info.items())



# 10.判断
# 空格强制缩进
# 语法:
# if bool条件:
#     True执行
#     else:
#         False执行

flag = True
if flag == True:
    print("出门浪")
else:
    print("考虑一下")

num1 = 10000
if num>=15000:
    print("打死也不出门")
    else:
        print("考虑一下");
