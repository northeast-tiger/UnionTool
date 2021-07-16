"""
距离计算模块
"""
from geopy import distance


class Dis(object):
    '''
    计算两地的直线距离
    '''

    def __init__(self):
        pass

    def object_distance(self, lat_lon_one, lat_lon_two, unit='km'):
        '''
        计算两地之间的直线距离
        :param lat_lon_one: 类型tuple，eg:(lat,lon)
        :param lat_lon_two: 类型tuple，eg:(lat,lon)
        :param unit: 单位：默认是千米
        :return: 小数点后保留四位有效数字
        '''
        if unit == "km":
            distance1 = distance.distance(lat_lon_one, lat_lon_two).km  # 算出来公里
            return str(round(distance1, 4)) + 'km'
        elif unit == 'nm':
            distance1 = distance.distance(lat_lon_one, lat_lon_two).nm  # 算出来海里
            return str(round(distance1, 4)) + 'nm'
        else:
            raise ValueError("未指定正确的单位")