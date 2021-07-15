# 处理时间示例文件
from src.TimeModule import TimeModule   # 导入文件


tm = TimeModule()

# 时间戳转北京时间   eg:-1893436000<====>1910-01-01 13:33:20
bj_time = tm.unix2bj(-1893436000)
print(bj_time)

# 北京时间转时间戳
'%Y/%m/%d %H:%M:%S'
print(tm.bj2unix("1910","%Y"))  # 年
print(tm.bj2unix("1910/01","%Y/%m"))  # 年/月
print(tm.bj2unix("1910-01-01","%Y-%m-%d"))  # 年-月-日
print(tm.bj2unix("1910/01/01 13:33:20","%Y/%m/%d %H:%M:%S"))  # 年/月/日 小时/分钟/秒