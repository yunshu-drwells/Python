import math
latitude1 = math.radians(float(input()))
longitude1 = math.radians(float(input()))
latitude2 = math.radians(float(input())) #纬度
longitude2 = math.radians(float(input())) #经度

#经纬度转换弧度

def har(th):
    return math.pow(math.sin(th/2), 2)

#求差值
vlon = abs(longitude1 - longitude2)
vlat = abs(latitude1 - latitude2)

h = har(vlat)+math.cos(latitude1)*math.cos(latitude2)*har(vlon)
print("{:.4f}".format(2*6371*math.asin(math.sqrt(h))), "km", sep = "")



import math
latitude1 = math.radians(float(input()))
longitude1 = math.radians(float(input()))
latitude2 = math.radians(float(input())) #纬度
longitude2 = math.radians(float(input())) #经度
def har(th):
    return math.pow(math.sin(th/2), 2)
vlon = abs(longitude1 - longitude2)
vlat = abs(latitude1 - latitude2)
print("{:.4f}".format(2*6371*math.asin(math.sqrt(har(vlat)+math.cos(latitude1)*math.cos(latitude2)*har(vlon)))), "km", sep = "")
