from src import Distance

# 实例化距离计算模块
dis  = Distance.Dis()
lat_lon_one=(12,34) #纬度在前，经度在后
lat_lon_two = (12,56)
res  = dis.object_distance(lat_lon_one,lat_lon_two,unit='nm')  # nm为海里，km为公里
print(res)