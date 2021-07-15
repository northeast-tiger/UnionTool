"""
时间处理模块，暂时支持：
    1)时间戳转北京时间
    2）北京时间转时间戳
支持1970年之前的转换
示例文件地址：Examples/deal_time
"""
import datetime


class TimeModule(object):
    '''
    时间转换模块
    '''

    def unix2bj(self, unix):
        '''
        时间戳转北京时间
        :param unix:时间戳   秒
        :return:北京时间
        '''
        unix = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=unix + 8 * 3600)  # 北京时间
        return unix

    def bj2unix(self, bj_time,format):
        '''
        北京时间转时间戳
        :param bj_time:北京时间  str类型
        :param format:时间格式  '%Y/%m/%d %H:%M:%S'
        :return:时间戳
        时间格式  '%Y/%m/%d %H:%M:%S'
        %Y  年
        %m  月
        %d  天
        %H  小时
        %M  分钟
        %S  秒数
        '''
        dateTime_p = datetime.datetime.strptime(bj_time, format)
        metTime = dateTime_p - datetime.datetime(1970, 1, 1)
        date_tample = metTime.days * 24 * 3600 + metTime.seconds - 28800  # 换算成秒数
        return date_tample